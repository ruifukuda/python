num = int(input('正の整数 >>'))
ls = []
for n in range(1, num + 1):
    ls.append(n)
print(sum(ls))

total = 0
for i in range(1, n + 1):
    total += i
print(total)

# 1行で終わることに気づけなかった
print(sum(range(1, n + 1)))
