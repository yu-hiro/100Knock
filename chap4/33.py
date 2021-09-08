from chap4_neko import neko_mapping

filename = 'data/neko.txt.mecab'

def main():
    sentences = neko_mapping(filename)
    result = set()
    for sentence in sentences:
        for i in range(1,len(sentence)-1):
            if sentence[i-1]['pos'] == '名詞' and sentence[i]['surface'] == 'の' and sentence[i+1]['pos'] == '名詞':
                result.add(sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface'])

    print(f'「名詞+の+名詞」の種類: {len(result)}')
    print('結果(一部)')
    for i in list(result)[:10]:
        print(i)


if __name__ == '__main__':
    main()
