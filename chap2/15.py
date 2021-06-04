import sys

filepath = 'data/popular-names.txt'

with open(filepath,'r') as r:

    # コマンドライン引数で出力する行数を指定
    N = sys.argv[1]

    # ファイル全体を行ごとに分割したリストを取得
    data = r.readlines()

    # 末尾のN行を出力する
    print(''.join(data[-1 * int(N):]))