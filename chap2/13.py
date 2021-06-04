r_filename1 = 'data/col1.txt'
r_filename2 = 'data/col2.txt'
w_filename = 'data/col_merge.txt'

with open(r_filename1,'r') as r1, open(r_filename2,'r') as r2, open(w_filename,'w') as w:
    # col1、col2から一行ずつ読み込み、処理する
    for data1 in r1:
        data2 = r2.readline()
        
        # ファイルに保存
        w.write(data1.strip() + '\t' + data2.strip() + '\n')
