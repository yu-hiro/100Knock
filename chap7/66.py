from gensim.models import KeyedVectors
import pandas as pd
from scipy.stats import spearmanr

words_filename = 'data/GoogleNews-vectors-negative300.bin.gz'
data_fileneme = 'data/combined.csv'

def main():
    # データ読み込み
    model = KeyedVectors.load_word2vec_format(words_filename, binary=True)
    df = pd.read_csv(data_fileneme, header=0)

    # 各行についてコサイン類似度を計算
    simi = []
    for i in range(len(df)):
        data = df.iloc[i]
        simi.append(model.similarity(data['Word 1'], data['Word 2']))
    df['similarity'] = simi

    # スピアマン相関係数を計算
    human = df['Human (mean)']
    similarity = df['similarity']
    correlation, pvalue = spearmanr(human, similarity)
    print('スピアマン相関係数:', correlation)


if __name__ == '__main__':
    main()
