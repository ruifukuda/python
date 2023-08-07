initial = 'K'
if initial == 'K':
    print('OK1')
else:
    print('NG1')

point = 82
if 80 <= point < 256:
    print('OK2')
else:
    print('NG2')

bmi = 24
if bmi < 20 or 25 < bmi:
    print('OK3')
else:
    print('NG3')

year = 2023
if year % 4 == 0:
    print('OK4')
else:
    print('NG4')

day = 30 
# if not (day == 28 or day == 30 or day == 31):
# if day not in[28, 30, 31]:
if not (day in[28, 30, 31]):
    print('OK5')
else:
    print('NG5')
