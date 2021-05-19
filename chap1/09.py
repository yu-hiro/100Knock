import random

def Typoglycemia(text):
    words = text.split()
    result = []
    for i in words:
        if len(i) <= 4:
            result.append(i)
        else:
            chr_list = list(i[1:-1])
            random.shuffle(chr_list)
            result.append(i[0] + ''.join(chr_list) + i[-1])
    return ' '.join(result)

text = input('入力文字列:')
result = Typoglycemia(text)
print('出力結果:' + result)