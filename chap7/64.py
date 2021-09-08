from gensim.models import KeyedVectors

words_filename = 'data/GoogleNews-vectors-negative300.bin.gz'
valid_filename = 'data/questions-words.txt'
write_filename = 'data/64.txt'

def main():
    # 単語ベクトルの読み込み
    model = KeyedVectors.load_word2vec_format(words_filename, binary=True)

    # 1行ずつ処理
    with open(valid_filename,'r') as f, open(write_filename,'w') as w:
        for line in f:
            line = line.split()

            if line[0] == ':': # カテゴリの行
                w.write(' '.join(line + ['\n']))
            else: # それ以外
                word, simi = model.most_similar(positive=[line[1], line[2]], negative=[line[0]], topn=1)[0]
                w.write(' '.join(line + [word, str(simi) + '\n']))


if __name__ == '__main__':
    main()