filepath = 'data/popular-names.txt'

with open(filepath,'r') as f:

    # 行数をカウント
    print('行数:',len(f.readlines()))