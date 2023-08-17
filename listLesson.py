import random


ls = [4, 10, 2, 5, 7]
print(ls)  # [4, 10, 2, 5, 7]
print(len(ls))  # 5
print(ls[0])  # 4
print(ls[-1])  # 7

for i in ls:
    print(i)

ls[0] = 1  # 要素の更新

ls.append(10)  # 末尾に追加

del ls[-1]  # リストの最後の要素削除

n = ls.pop()  # リストの末尾を削除して、nに代入
n = ls.pop(0)  # 先頭を削除してnに代入

ls2 = [1, 2, 3]
ls3 = [4, 5, 6]
ls4 = ls2 + ls3  # [1, 2, 3, 4, 5, 6]

ls5 = ls2 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ちゃんと覚えとけ、必要なときに曖昧で使えないから
ls6 = [3, 1, 4, 8]
print(ls6)

ls7 = sorted(ls6)  # 昇順ソート、元のリストは変更されない
print(ls7)
ls7.sort()  # 昇順ソート、破壊的処理
print(ls7)

ls8 = sorted(ls7, reverse=True)  # 降順ソート、元変更なし
print(ls8)
ls8.sort(reverse=True)  # 降順ソート、破壊的処理
print(ls8)

ls9 = list(reversed(ls8))  # 逆順に取り出すイテレータ
print(ls9)
ls9.reverse()  # 逆順並び替え、破壊的処理
print(ls9)

ls10 = [1, 2, 3, 4, 5]
random.shuffle(ls10)  # シャッフル完了
print(ls10)

data = ['大吉', '中吉', '吉', '凶']
result = random.choice(data)  # ランダムに1個選択
print(result)
