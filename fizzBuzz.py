for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

msg = 'hello'
ls = list(msg)
print(ls)

word = input('英単語 >>')
ls = list(word)
if len(word) == len(set(ls)):
    print('同じアルファベットは含まれていない')
else:
    print('同じアルファベットが含まれている')
