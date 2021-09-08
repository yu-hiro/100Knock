from chap4_neko import neko_mapping

filename = 'data/neko.txt.mecab'

def main():
    sentences = neko_mapping(filename)
    result = set()
    for sentence in sentences:
        for i in sentence:
            if i['pos'] == '動詞':
                result.add(i['surface'])

    print(f'動詞の表層形の種類: {len(result)}')
    print('結果(一部)')
    for i in list(result)[:10]:
        print(i)



if __name__ == '__main__':
    main()
