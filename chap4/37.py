from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

filename = 'data/neko.txt.mecab'

def neko_mapping(filename):
    neko = []
    morphs = []
    with open(filename, 'r', encoding='utf-8_sig') as r: # Windows上で実行したので、'utf-8_sig'で指定
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

# 「猫」と共起頻度が高い単語
def neko_co_freq(sentences):
    result = defaultdict(int)
    for sentence in sentences:
        if '猫' in [i['surface'] for i in sentence]:
            for i in sentence:
                if i['pos'] != '記号':
                    result[i['base']] += 1
    del result['猫']
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return result

def main():
    sentences = neko_mapping(filename)
    result = neko_co_freq(sentences)

    # グラフを描く
    x = [a[0] for a in result[0:10]]
    y = [a[1] for a in result[0:10]]
    plt.figure(figsize=(8, 4))
    plt.bar(x,y)
    plt.show()  # 表示する場合
    # plt.savefig('37_fig.png') # 画像保存する場合

if __name__ == '__main__':
    main()