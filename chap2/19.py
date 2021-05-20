from itertools import groupby

filepath = 'data/popular-names.txt'

with open(filepath,'r') as r:

    # ファイル全体を行ごとに分割したリストを取得
    lines = r.readlines()

    # 各行の1列目を取得したリストを作成
    names = [line.split('\t')[0] for line in lines]

    # 作成したリストをソート
    names.sort()

    # リストの要素をグループ化し、出現頻度を計算
    result = [(name,len(list(group))) for name,group in groupby(names)]

    # 出現頻度の高い順にソート
    result.sort(key=lambda name: name[1], reverse=True)

    # 結果を出力
    for data in result:
        print('{name} {c}'.format(name=data[0],c=data[1]))