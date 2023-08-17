import random


ls = [random.randint(0, 100) for _ in range(100)]
print(ls)
print(len(ls))

ls.sort(reverse=True)
# ls[0:10]の前の0いらない
print(ls[:10])

# sortedなら1行でできた
print(sorted(ls, reverse=True)[:10])
