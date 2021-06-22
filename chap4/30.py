filename = 'data/neko.txt.mecab'

result = []
morphs = []
with open(filename, 'r') as r:
    for line in r: # 1行ずつ読み込む
        if line != 'EOS\n': # 文末でない場合
            fields = line.split('\t')
            if len(fields) != 2 or fields[0] == '': # 文頭以外の空白と改行文字はスキップ
                continue
            else:
                attr = fields[1].split(',')
                morph = {'surface':fields[0], 'base':attr[6],
                         'pos':attr[0], 'pos1':attr[1]}
                morphs.append(morph)
        else:
            result.append(morphs)
            morphs = []

for i in result[2]:
    print(i)