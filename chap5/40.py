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

def main():
    result = []
    morphs = []

    with open(filename, 'r') as r:
        for line in r:
            if line[0] == '*': # 係り受け関係の行
                continue
            elif line != 'EOS\n': # 文末以外
                morphs.append(Morph(line))
            else: # 文末
                result.append(morphs)
                morphs = []

    # 確認
    for i in result[2]:
        print(vars(i))


if __name__ == '__main__':
    main()