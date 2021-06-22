filename = 'data/neko.txt.mecab'

def neko_mapping(filename):
    neko = []
    morphs = []
    with open(filename, 'r') as r:
        for line in r: # 1行ずつ読み込む
            if line != 'EOS\n': # 文末でない場合
                fields = line.split('\t')
                if len(fields) != 2 or fields[0] == '': # 文頭以外の空白と改行文字はスキップ
                    continue
                else:
                    attr = fields[1].split(',')
                    morph = {'surface': fields[0], 'base': attr[6],
                             'pos': attr[0], 'pos1': attr[1]}
                    morphs.append(morph)
            else:
                neko.append(morphs)
                morphs = []
    return neko

def main():
    sentences = neko_mapping(filename)
    result = set()
    for sentence in sentences:
        for i in range(1,len(sentence)-1):
            if sentence[i-1]['pos'] == '名詞' and sentence[i]['surface'] == 'の' and sentence[i+1]['pos'] == '名詞':
                result.add(sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface'])

    print(f'「名詞+の+名詞」の種類: {len(result)}')
    print('結果(一部)')
    for i in list(result)[:10]:
        print(i)


if __name__ == '__main__':
    main()