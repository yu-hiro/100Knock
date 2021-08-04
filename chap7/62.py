from gensim.models import KeyedVectors

filename = 'data/GoogleNews-vectors-negative300.bin.gz'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(filename, binary=True)

    # 'United States'とコサイン類似度が高い10語と,その類似度を計算
    result = model.most_similar('United_States', topn=10)
    print(result)


if __name__ == '__main__':
    main()