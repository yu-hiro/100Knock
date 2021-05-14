def temp(x, y, z):
    result = '{}時の{}は{}'.format(x, y, z)
    return result


print('出力結果:' + temp(x=12, y='気温', z=22.4))