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

# ファイルの参照行か調べる
def is_file(s):
    return re.match(r'^\[\[:*(ファイル|File):.*\]\]$',s)

# ギャラリーのファイル部分か調べる
def is_file_gal(s):
    return re.match(r'^(ファイル|File):.*\]\]',s)

def main():
    text = read_Eng(filepath).split('\n')

    print('ファイル参照')
    for line in text:
        # ファイル参照の行を出力する
        if is_file(line):
            fi = re.match(r'^\[\[:*(?:ファイル|File):(.+)\|.+\]\]$',line)
            print(fi.group(1))
        elif is_file_gal(line):
            fi = re.match(r'^(?:ファイル|File):(.+)\|.+$',line)
            print(fi.group(1))

if __name__ == '__main__':
    main()