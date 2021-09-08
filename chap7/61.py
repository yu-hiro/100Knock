from gensim.models import KeyedVectors

filename = 'data/GoogleNews-vectors-negative300.bin.gz'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(filename, binary=True)

    # 'United States'と'U.S.'のコサイン類似度を計算
    result = model.similarity('United_States', 'U.S.')
    print(result)


if __name__ == '__main__':
    main()