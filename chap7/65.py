filename = 'data/64.txt'

def main():
    flag = 0
    sem_cnt = 0
    sem_true = 0
    syn_cnt = 0
    syn_true = 0

    with open(filename, 'r') as f:
        for line in f:
            line = line.split()

            if len(line) == 2: # カテゴリの行
                if 'gram' in line[1]: # 意味的アナロジーのブロック
                    flag = 0
                else: # 文法的アナロジーのブロック
                    flag = 1
            elif flag == 0:
                sem_cnt += 1
                if line[3] == line[4]:
                    sem_true += 1
            else:
                syn_cnt += 1
                if line[3] == line[4]:
                    syn_true += 1

    print('意味的アナロジーの正解率:', sem_true/sem_cnt)
    print('文法的アナロジーの正解率:', syn_true/syn_cnt)


if __name__ == '__main__':
    main()