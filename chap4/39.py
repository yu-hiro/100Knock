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

# 単語の出現頻度
def word_freq(sentences):
    result = defaultdict(int)
    for sentence in sentences:
        for i in sentence:
            if i['pos'] != '記号':
                result[i['base']] += 1

    # 結果をソート
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return result

def main():
    sentences = neko_mapping(filename)
    result = word_freq(sentences)

    # 両対数グラフを描く
    x = [a + 1 for a in range(len(result))]
    y = [a[1] for a in result]
    plt.figure(figsize=(8, 4))
    plt.scatter(x, y) # 散布図を描く
    plt.xscale('log') # 対数軸で表示
    plt.yscale('log')
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    plt.show() # 表示する場合
    #plt.savefig('39_fig.png') # 画像保存する場合

if __name__ == '__main__':
    main()