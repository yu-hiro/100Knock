from gensim.models import KeyedVectors

filename = 'data/GoogleNews-vectors-negative300.bin.gz'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(filename, binary=True)

    # 'United States'の単語ベクトルを表示
    print(model['United_States'])

if __name__ == '__main__':
    main()