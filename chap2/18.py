filepath = 'data/popular-names.txt'

with open(filepath,'r') as r:

    # ファイル全体を行ごとに分割したリストを取得
    lines = r.readlines()

    # 各行を3列目の数値の降順にソート
    lines.sort(key=lambda line:int(line.split('\t')[2]),reverse=True)

    # 結果を出力する
    for i in lines:
        print(i)