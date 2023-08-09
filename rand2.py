import random


count = 0
while True:
    count += 1
    number = random.randint(1, 9999)
    print(f'{count}: {number}')
    if number == 7777:
        break
print(f'{count}回目に7777がでました!')
