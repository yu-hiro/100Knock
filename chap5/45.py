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

    # 45の内容
    with open('result45.txt', 'w') as w:
        for sentence in sentences:
            for chunk in sentence:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        cases = []
                        for src in chunk.srcs: # 見つけた動詞の係り元のchunkから助詞を探す
                            cases = cases + [morph.surface for morph in sentence[src].morphs if morph.pos == '助詞']
                        if len(cases) > 0: # 助詞が見つかった場合、重複を除去して辞書順にソートする
                            cases = sorted(list(set(cases)))
                            line = '{}\t{}'.format(morph.base, ' '.join(cases))
                            print(line, file=w)
                        break


if __name__ == '__main__':
    main()