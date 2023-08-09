def plus(x, y):
    answer = x + y
    return answer


ans = plus(100, 50)
print(f'足し算の答えは{ans}です')

hoge = plus  # plus関数の参照値をコピーしている
n = hoge(5, 8)
print(f'足し算の答えは{ans}です')
