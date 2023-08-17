def weather():
    print('今日は晴れです')


def calc_circle_area(r: float) -> float:
    return r * r * 3.14


def nowstr():
    return '18時25分30秒'


def nowint() -> tuple:
    return (18, 25, 30)


def is_leapyear(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


weather()
print(calc_circle_area(2))
print(nowstr())
h, m, s = nowint()
print(h, m, s)
print(is_leapyear(2023))
print(is_leapyear(2020))

year = int(input('何年>>'))
if (is_leapyear(year)):
    print(f'西暦{year}年は閏年です')
else:
    print(f'西暦{year}年は閏年ではありません')
