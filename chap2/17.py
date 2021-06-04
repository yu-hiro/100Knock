filepath = 'data/popular-names.txt'

with open(filepath,'r') as r:

    # 結果の集合
    result = set()

    # 一行ずつ読み込む
    for line in r:

        # 行をタブで区切る
        cols = line.split('\t')

        # 集合に要素を追加
        result.add(cols[0])

    # 結果を出力
    for i in result:
        print(i)