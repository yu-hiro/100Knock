from chap4_neko import neko_mapping
from collections import defaultdict
import matplotlib.pyplot as plt
import japanize_matplotlib

filename = 'data/neko.txt.mecab'

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
