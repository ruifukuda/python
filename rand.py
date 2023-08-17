import random

num = random.randint(5, 10)  # 5~10の値をランダムに1個生成
print(num)  # 8


dices = []
count = int(input('何回振る? >>'))
# for n in numberって書いてエラー、range(number)じゃないとダメ
for _ in range(count):
    dice = random.randint(1, 6)
    # result.append = diceって書いてエラー、3分間違いに気づかない
    dices.append(dice)
print(dices)
# sum(リスト)で合計出る、わざわざfor文の中で足しこんでいく必要ない
# というかsum = 0にするとsum関数上書きするから最悪
print(f'合計は{sum(dices)}でした')
