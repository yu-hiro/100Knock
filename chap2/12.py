r_filename = 'data/popular-names.txt'
w_filename1 = 'data/col1.txt'
w_filename2 = 'data/col2.txt'

with open(r_filename,'r') as r:
    with open(w_filename1,'w') as w1:
        with open(w_filename2,'w') as w2:

            # 一行ずつ読み込む
            for line in r:

                # タブで区切り、配列化
                col = line.strip().split('\t')

                # 1列目、2列目を保存
                w1.write(col[0] + '\n')
                w2.write(col[1] + '\n')