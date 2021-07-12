from itertools import combinations
import re

filename = 'data/ai.ja.txt.parsed'

# 形態素クラス
class Morph:
    def __init__(self, line):
        fields = line.split('\t')
        attr = fields[1].split(',')

        self.surface = fields[0]
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]

# 文節クラス
class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.srcs = []
        self.dst = dst

def main():
    morphs = []
    chunks = []
    sentences = []

    with open(filename, 'r') as r:
        for line in r:
            if line[0] == '*': # 係り受け関係の行
                if len(morphs) > 0:
                    chunks.append(Chunk(morphs, dst))
                    morphs = []
                dst = int(line.split(' ')[2].rstrip('D'))
            elif line != 'EOS\n': # 文末以外
                morphs.append(Morph(line))
            else: # 文末
                chunks.append(Chunk(morphs, dst))
                for i, chunk in enumerate(chunks):
                    if chunk.dst not in [None, -1]:
                        chunks[chunk.dst].srcs.append(i)
                sentences.append(chunks)
                morphs = []
                chunks = []
                dst = None

    # 49の内容
    sen49 = sentences[2]
    nouns = []
    for i, chunk in enumerate(sen49):
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            nouns.append(i)
    for i, j in combinations(nouns, 2):  # 名詞を含む文節のペアごとにパスを作成
        path_i = []
        path_j = []
        while i != j:
            if i < j:
                path_i.append(i)
                i = sen49[i].dst
            else:
                path_j.append(j)
                j = sen49[j].dst
        if len(path_j) == 0: # 1つ目(文節iから構文木の根に至る経路上に文節jが存在する場合)
            chunk_X = ''.join(
                [morph.surface if morph.pos != '名詞' else 'X' for morph in sen49[path_i[0]].morphs])
            chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sen49[i].morphs])
            chunk_X = re.sub('X+', 'X', chunk_X)
            chunk_Y = re.sub('Y+', 'Y', chunk_Y)
            path_XtoY = [chunk_X] + [''.join(morph.surface for morph in sen49[n].morphs) for n in
                                     path_i[1:]] + [chunk_Y]
            print(' -> '.join(path_XtoY)) # 文節iから文節jのパスを表示
        else: # 2つ目のケース(1つ目のケース以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合)
            chunk_X = ''.join(
                [morph.surface if morph.pos != '名詞' else 'X' for morph in sen49[path_i[0]].morphs])
            chunk_Y = ''.join(
                [morph.surface if morph.pos != '名詞' else 'Y' for morph in sen49[path_j[0]].morphs])
            chunk_k = ''.join([morph.surface for morph in sen49[i].morphs])
            chunk_X = re.sub('X+', 'X', chunk_X)
            chunk_Y = re.sub('Y+', 'Y', chunk_Y)
            path_X = [chunk_X] + [''.join(morph.surface for morph in sen49[n].morphs) for n in path_i[1:]]
            path_Y = [chunk_Y] + [''.join(morph.surface for morph in sen49[n].morphs) for n in path_j[1:]]
            # 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス、文節kの内容を'|'で連結して表示
            print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]))


if __name__ == '__main__':
    main()