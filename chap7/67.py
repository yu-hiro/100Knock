from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np

filename = 'data/GoogleNews-vectors-negative300.bin.gz'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(filename, binary=True)

    # 国名を取得する
    flag = 2
    countries = set()
    with open('data/questions-words.txt','r') as f:
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

    # k-meansクラスタリング
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(countries_v)
    for i in range(5):
        cluster = np.where(kmeans.labels_ == i)[0]
        print('cluster', i)
        print(', '.join([countries[k] for k in cluster]))


if __name__ == '__main__':
    main()