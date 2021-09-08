from chap4_neko import neko_mapping
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

filename = 'data/neko.txt.mecab'

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
