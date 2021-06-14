import gzip
import json
import re
import urllib.parse, urllib.request

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

        # {{...}}を除去する
        #lang
        r4 = re.compile(r'\{\{lang\|(.+?)\}\}')
        j = r4.sub(lambda m: m.group(1).split('|')[-1], j)
        #icon
        r4 = re.compile(r'\{\{.+\sicon\}\}')
        j = r4.sub('', j)
        #その他
        r4 = re.compile(r'\{\{(.+?)\}\}')
        j = r4.sub(lambda m: m.group(1).split('|')[-1], j)

        # 内部リンクマークアップを除去する
        r2 = re.compile(r'\[\[([^]]+)\]\]')
        j = r2.sub(lambda m: m.group(1).split('|')[-1], j)

        # 外部リンクを除去する
        r3 = re.compile(r'\[https?[^]]+\>[^]]+\]')
        j = r3.sub('',j)
        r3 = re.compile(r'\[https?([^]]+)\]')
        j = r3.sub(lambda m: m.group(1).split(' ')[-1], j)

        # HTMLタグを除去する
        r5 = re.compile(r'\<.+?\>')
        j = r5.sub(' ', j)

        # 箇条書きを除去する
        r6 = re.compile(r'\*+')
        j = r6.sub('',j)

        basic_info[i] = j

    # 国旗画像の値を取得
    flag = basic_info['国旗画像']

    # リクエストを生成
    url = 'https://www.mediawiki.org/w/api.php?' \
        + 'action=query' \
        + '&titles=File:' + urllib.parse.quote(flag) \
        + '&format=json' \
        + '&prop=imageinfo' \
        + '&iiprop=url'

    # MediaWikiのサービスへリクエストを送信
    request = urllib.request.Request(url,
                                     headers={'User-Agent': 'NLP100_Python(@segavvy)'})
    connection = urllib.request.urlopen(request)

    # jsonとして受信
    data = json.loads(connection.read().decode())

    # URLを取り出す
    url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']

    print(url)

if __name__ == '__main__':
    main()