# 文字n-gram
def char_n_gram(s,N):
    chars = s.replace(' ','')
    result = []
    for i in range(len(chars)):
        if i+N > len(chars):
            return result
        else:
            result.append(chars[i:i+N])

X = set(char_n_gram('paraparaparadise',N=2))
print('X')
print(X)
Y = set(char_n_gram('paragraph',N=2))
print('Y')
print(Y)

XY_union = X | Y
print('和集合')
print(XY_union)
XY_intersection = X & Y
print('積集合')
print(XY_intersection)
XY_difference = X - Y
print('差集合(X-Y)')
print(XY_difference)
YX_difference = Y - X
print('差集合(Y-X)')
print(YX_difference)

print('seが含まれるか')
if 'se' in X:
    print('X:Yes')
else:
    print('X:No')
if 'se' in Y:
    print('Y:Yes')
else:
    print('Y:No')