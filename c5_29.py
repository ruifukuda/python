def eat(breakfast, lunch, dinner, *desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')
    print(desserts)
    for d in desserts:
        print(f'おやつに{d}を食べました')


print('8月1日')
eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')


def sumof(*args):
    total = 0
    for i in args:
        total += i
    return total


print(sumof(5, 3, 9))
