import sys

filepath = 'data/popular-names.txt'

with open(filepath,'r') as r:

    # コマンドライン引数で分割数を指定
    N = sys.argv[1]

    # ファイル全体を行ごとに分割したリストを取得
    lines = r.readlines()

    # ファイルを何行ごとに分割するか計算
    split_line = len(lines) // int(N)

    # ファイルをN分割する
    for i in range(int(N)):
        offset = i * split_line
        text = lines[offset:offset + split_line]

        # ファイルに保存
        save_filename = 'data/popular-names_{:03d}.txt'.format(i)
        with open(save_filename,'w') as w:
            w.write(''.join(text))