from chap4_neko import neko_mapping
from collections import defaultdict

filename = 'data/neko.txt.mecab'

def main():
    sentences = neko_mapping(filename)
    result = defaultdict(int)
    for sentence in sentences:
        for i in sentence:
            if i['pos'] != '記号':
               result[i['base']] += 1

    # 結果をソート
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    print('単語の出現頻度(上位10個)')
    for i in result[:10]:
        print(i)


if __name__ == '__main__':
    main()
