month = int(input('今は何月ですか? (数字を入力) >>'))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print('31日までありますね')
else:
    if month != 2:
        print('30日までですね')
    else:
        print('1年で一番寒い月ですね')
    print('年が空けてから')
print(f'{month}箇月が過ぎました')

"""
int n = 4;
String result = n % 2 == 0 ? "偶数" : "奇数";
System.out.println(result)
"""
