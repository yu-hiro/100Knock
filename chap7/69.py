from gensim.models import KeyedVectors
import bhtsne
import numpy as np
import matplotlib.pyplot as plt

filename = 'data/GoogleNews-vectors-negative300.bin.gz'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(filename, binary=True)

    # 国名を取得する
    flag = 2
    countries = set()
    with open('data/questions-words.txt', 'r') as f:
        for line in f:
            line = line.split()

            if len(line) == 2:  # カテゴリの行
                if line[1] in ['capital-common-countries', 'capital-world']:
                    flag = 1
                elif line[1] in ['currency', 'gram6-nationality-adjective']:
                    flag = 0
                else:
                    flag = 2
            elif flag == 1:
                countries.add(line[1])
            elif flag == 0:
                countries.add(line[0])
            else:
                continue
        countries = list(countries)

    # 単語ベクトルを取得
    countries_v = [model[country] for country in countries]

    # t-SNEで可視化
    ts = bhtsne.tsne(np.array(countries_v).astype(np.float64), dimensions=2, rand_seed=42)
    plt.scatter(np.array(ts).T[0], np.array(ts).T[1])
    for (x, y), name in zip(ts, countries):
        plt.annotate(name, (x, y))
    # plt.show()
    plt.savefig('69_fig.png')  # 画像保存する場合


if __name__ == '__main__':
    main()