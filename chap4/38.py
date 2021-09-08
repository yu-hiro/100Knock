from chap4_neko import neko_mapping
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

filename = 'data/neko.txt.mecab'

# ヒストグラム
def word_hist(sentences):
    result = defaultdict(int)
    for sentence in sentences:
        for i in sentence:
            if i['pos'] != '記号':
                result[i['base']] += 1
    result = result.values()
    return result

def main():
    sentences = neko_mapping(filename)
    result = word_hist(sentences)

    # ヒストグラムを描く
    plt.figure(figsize=(8, 4))
    plt.hist(result, bins=100)
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')
    plt.show()  # 表示する場合
    # plt.savefig('38_fig.png') # 画像保存する場合

if __name__ == '__main__':
    main()
