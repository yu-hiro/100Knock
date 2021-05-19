def cipher(text):
    result = ''
    for i in text:
        if i.islower():
            result += chr(219-ord(i))
        else:
            result += i
    return result

text = input('入力文字列:')
result1 = cipher(text)
print('暗号化:' + result1)
result2 = cipher(result1)
print('復号化:' + result2)