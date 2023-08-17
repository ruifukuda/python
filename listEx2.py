import pprint


data1 = [[i - j for j in range(10)] for i in range(100, 0, -10)]
pprint.pprint(data1)

data2 = [[1 if i == j or i + j == 4 else 0 for j in range(5)]
         for i in range(5)]
pprint.pprint(data2)

# range(0, 10)ってrange(10)だよ
data3 = [[i * 10 - j * 10 for j in range(10)] for i in range(10)]
pprint.pprint(data3)

data4 = [[1 if i == j else 2 if i > j else 0
          for j in range(5)]
         for i in range(5)]
pprint.pprint(data4)

data5 = [[i + 1 if i == j else 0
          for j in range(4)] for i in range(4)]
pprint.pprint(data5)

data6 = [[i + j for j in range(9)] for i in range(60, 91, 10)]
pprint.pprint(data6)

data7 = [[i * j for j in range(1, 10)] for i in range(1, 10)]
pprint.pprint(data7)

data8 = [[3 if i == 1 and j == 1 else 7 for j in range(3)]
         for i in range(3)]
pprint.pprint(data8)

data9 = [[i * j for j in range(1, 10)] for i in range(3, 10, 2)]
pprint.pprint(data9)

data10 = [[i + j * 2 for j in range(5)] for i in range(2, 0, -1)]
pprint.pprint(data10)

# 'も表示されるから'\'*\''って書く必要ない
data11 = [['*' if i % 2 == 0 and j % 2 != 0
           else '_'
           for j in range(10)]
          for i in range(10)]
pprint.pprint(data11)

data12 = [[i ** 2 + j for j in range(10)] for i in range(10)]
pprint.pprint(data12)

data13 = [[i - j for j in range(i)] for i in range(10, 0, -1)]
pprint.pprint(data13)
