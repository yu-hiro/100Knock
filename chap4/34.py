from chap4_neko import neko_mapping

filename = 'data/neko.txt.mecab'

def main():
    sentences = neko_mapping(filename)
    result = set()
    for sentence in sentences:
        nouns = ''
        count = 0
        for i in sentence:
            if i['pos'] == '名詞': # 名詞
                nouns = ''.join([nouns,i['surface']])
                count += 1
            elif count >= 2: # 名詞以外で、これまでの連結数が2以上
                result.add(nouns)
                nouns = ''
                count = 0
            else: # それ以外
                nouns = ''
                count = 0
        if count >= 2:
            result.add(nouns)

    print(f'連接名詞の種類: {len(result)}')
    print('結果(一部)')
    for i in list(result)[:10]:
        print(i)


if __name__ == '__main__':
    main()
