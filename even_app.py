start = int(input('start>>'))
end = int(input('end>>'))


for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=' ')
print()


# リストから中身だけ表示させる方法分からなくてもたもた
# 3行
ls = [i for i in range(start, end + 1) if i % 2 == 0]
[print(n, end=' ') for n in ls]
print()

# 2行だけどパッと見意味不明
[print(i, end=' ') for i in range(start, end + 1) if i % 2 == 0]
print()

# .join()は数字扱えないからstr()で変換しとかないといけない
ls = [str(i) for i in range(start, end + 1) if i % 2 == 0]
print(' '.join(ls))

# 改行されてる
print('a')

# リストの中にリスト作って渡す側で*つけてアンパックして渡す
ls = [[i for i in range(start, end + 1) if i % 2 == 0]]
print(*ls[0])
