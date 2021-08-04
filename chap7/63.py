from gensim.models import KeyedVectors

filename = 'data/GoogleNews-vectors-negative300.bin.gz'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(filename, binary=True)

    # 'Spain'の単語ベクトルから'Madrid'のベクトルを引き,'Athens'のベクトルを足したベクトルと類似度の高い10語とその類似度を計算
    result = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
    print(result)


if __name__ == '__main__':
    main()