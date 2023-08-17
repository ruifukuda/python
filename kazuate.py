import random


ans = random.randint(1, 100)  # 答えを生成
MAX_COUNT = 5  # 試行回数
# print(type(MAX_COUNT))
print('1-100の数字の中から1つ選んだよ。')
print('その数字を', MAX_COUNT, '回以内に当ててね')

for i in range(1, MAX_COUNT+1):
    num = int(input(f'{i}回目、いくつかな'))
    if num == ans:
        print('当たり！！')
        break
    elif i == MAX_COUNT:  # 最後にもっと上とかいらないからpassさせる
        pass
    elif num > ans:
        print('もっと下だよ')
    else:
        print('もっと上だよ')
else:
    print('残念～正解は', ans, 'でした。')
