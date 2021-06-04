import gzip
import json

filepath = 'data/jawiki-country.json.gz'

# ファイルを解凍して読み込む
with gzip.open(filepath,'r') as r:

    for line in r:

        # 行のデータを読み込む
        data = json.loads(line)

        # イギリスに関する記事本文を出力する
        if data['title'] == 'イギリス':
            print(data['text'])