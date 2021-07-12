from graphviz import Digraph

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

    # with open(filename, 'r') as r:
    with open(filename, 'r', encoding='utf-8_sig') as r:  # Windows上で実行したので、'utf-8_sig'で指定
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

    # 44の内容
    sen44 = sentences[2]
    edges = []
    for id, chunk in enumerate(sen44):
        if int(chunk.dst) != -1:
            modifier = ''.join(
                [morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs] + ['(' + str(id) + ')'])
            modifiee = ''.join(
                [morph.surface if morph.pos != '記号' else '' for morph in sen44[int(chunk.dst)].morphs] + ['(' + str(chunk.dst) + ')'])
            edges.append([modifier, modifiee])

    # 有向グラフを作成
    dg = Digraph(format='png')
    dg.attr('node', shape='circle', fontname='MS Gothic')
    for i, j in edges:
        dg.edge(i, j)
    dg.render('44')


if __name__ == '__main__':
    main()