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

# セクション行か調べる
def is_section(s):
    return re.match(r'^=+.+=+$',s)

def main():
    text = read_Eng(filepath).split('\n')

    print('セクション名 (セクションレベル)')
    for line in text:
        # セクション名とレベルを出力する
        if is_section(line):
            se = re.match(r'^(=+)(.+)=+$',line)
            print('{} ({})'.format(se.group(2),len(se.group(1))-1))

if __name__ == '__main__':
    main()