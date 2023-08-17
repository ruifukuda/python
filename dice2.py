import random


print('サイコロ振ったよ')
dice1 = random.randint(1, 6)
print(f'1回目:{dice1}')
dice2 = random.randint(1, 6)
print(f'2回目:{dice2}')
if dice2 > dice1:
    print(f'2回目は1回目より{dice2 - dice1}大きいです')
elif dice2 < dice1:
    print(f'2回目は1回目より{dice1 - dice2}小さいです')
else:
    print('2回目は1回目と同じです')
