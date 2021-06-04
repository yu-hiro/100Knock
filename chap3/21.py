import gzip
import json
import re

filepath = 'data/jawiki-country.json.gz'

# イギリスに関する記事本文を返す
def read_Eng(filepath):
    with gzip.open(filepath, 'r') as r:
        for line in r:
            # 行のデータを読み込む
            data = json.loads(line)
            # イギリスに関する記事本文を出力する
            if data['title'] == 'イギリス':
                return data['text']

def main():
    text = read_Eng(filepath).split('\n')

    # カテゴリの行を出力
    for line in text:
        if re.match(r'^\[\[Category:.+\]\]$',line):
            print(line)


if __name__ == '__main__':
    main()