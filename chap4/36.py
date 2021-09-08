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

    # グラフを描く
    x = [a[0] for a in result[0:10]]
    y = [a[1] for a in result[0:10]]
    plt.figure(figsize=(8, 4))
    plt.bar(x,y)
    plt.show()  # 表示する場合
    # plt.savefig('36_fig.png') # 画像保存する場合

if __name__ == '__main__':
    main()
