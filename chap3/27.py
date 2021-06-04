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

# 基礎情報テンプレートを探す
def get_basic_info(s):
    # 基礎情報の中身を探す
    m = re.search(r'\{\{基礎情報[^|]+\|(.+?)\n\}\}',s,re.DOTALL)
    basic_info = m.group(1).split('\n|')

    templates = {}

    # フィールド名と値を辞書オブジェクトとして格納
    for item in basic_info:
        name, val = re.split(r'\s*=\s*',item,maxsplit=1)
        templates[name] = val

    return templates


def main():
    text = read_Eng(filepath)

    # 基礎情報テンプレートからデータを抽出
    basic_info = get_basic_info(text)

    for i, j in basic_info.items():

        # 強調マークアップを除去する
        r1 = re.compile(r'\'{2,}')
        j = r1.sub('', j)

        # 内部リンクマークアップを除去する
        r2 = re.compile(r'\[\[([^]]+)\]\]')
        j = r2.sub(lambda m: m.group(1).split('|')[-1], j)

        basic_info[i] = j

    print(basic_info)

if __name__ == '__main__':
    main()