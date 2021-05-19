s = 'I am an NLPer'

# 単語n-gram
def word_n_gram(s,N):
    words = s.split()
    result = []
    for i in range(len(words)):
        if i+N > len(words):
            return result
        else:
            result.append(words[i:i+N])

# 文字n-gram
def char_n_gram(s,N):
    chars = s.replace(' ','')
    result = []
    for i in range(len(chars)):
        if i+N > len(chars):
            return result
        else:
            result.append(chars[i:i+N])
print(s)
print('単語bi-gram')
print(word_n_gram(s,N=2))
print('文字bi-gram')
print(char_n_gram(s,N=2))