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

    # 48の内容
    sen48 = sentences[2]
    for chunk in sen48:
        if '名詞' in [morph.pos for morph in chunk.morphs]: # chunkが名詞を含むか調べる
            path = [''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')]
            while chunk.dst != -1: # 名詞を含むchunkを先頭にして、dstを根まで順に辿ってリストに追加する
                path.append(''.join(morph.surface for morph in sen48[chunk.dst].morphs if morph.pos != '記号'))
                chunk = sen48[chunk.dst]
            print(' -> '.join(path)) # 「->」でつなぐ


if __name__ == '__main__':
    main()