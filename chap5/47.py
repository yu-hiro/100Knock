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

    # 47の内容
    with open('result47.txt', 'w') as w:
        for sentence in sentences:
            for chunk in sentence:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        for i, src in enumerate(chunk.srcs): # 見つけた動詞の係り元のchunkが「サ変接続名詞+を」で構成されるか調べる
                            if len(sentence[src].morphs) == 2 and sentence[src].morphs[0].pos1 == 'サ変接続' and sentence[src].morphs[1].surface == 'を':
                                predicate = ''.join([sentence[src].morphs[0].surface, sentence[src].morphs[1].surface, morph.base])
                                cases = []
                                modi_chunks = []
                                for src_r in chunk.srcs[:i] + chunk.srcs[i + 1:]: # 残りの係り元chunkから助詞を探す
                                    case = [morph.surface for morph in sentence[src_r].morphs if morph.pos == '助詞']
                                    if len(case) > 0: # 助詞を含むchunkの場合は助詞と項を取得
                                        cases = cases + case
                                        modi_chunks.append(''.join(
                                            morph.surface for morph in sentence[src_r].morphs if morph.pos != '記号'))
                                if len(cases) > 0: # 助詞が1つ以上見つかった場合、重複を除去して辞書順にソート、項と一緒に出力
                                    cases = sorted(list(set(cases)))
                                    line = '{}\t{}\t{}'.format(predicate, ' '.join(cases), ' '.join(modi_chunks))
                                    print(line, file=w)
                                break


if __name__ == '__main__':
    main()