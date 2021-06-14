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

# カテゴリの行か調べる
def is_category(s):
    return re.match(r'^\[\[Category:.+\]\]$',s)

def main():
    text = read_Eng(filepath).split('\n')

    for line in text:
        if is_category(line):
            # カテゴリ名を抽出する
            ca = re.match(r'^\[\[Category:(.+)\]\]$',line)
            ca_name = ca.group(1).split('|')[0]
            print(ca_name)


if __name__ == '__main__':
    main()