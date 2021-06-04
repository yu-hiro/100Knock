filepath = 'data/popular-names.txt'

with open(filepath,'r') as f:

    # タブをスペースに変換                                              
    print(f.read().replace('\t',' '))