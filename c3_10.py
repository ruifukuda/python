print('すべての質問にyまたはnで答えてください')
okane_aruka = input('お金に余裕はありますか? >>')
if okane_aruka == 'y':
    onaka_suitaka = input('お腹がすごく空いてますか? >>')
    nomitai_kibunka = input('ビールを飲みたいですか? >>')
    if onaka_suitaka == 'y' and nomitai_kibunka == 'y':
        print('焼肉はいかがですか')
    elif onaka_suitaka == 'y':
        print('カレーはいかがですか')
    elif nomitai_kibunka == 'y':
        print('焼き鳥はいかがですか')
    else:
        print('パスタはいかがですか')
    yasyoku_iruka = input('夜食は必要ですか? >>')
    if yasyoku_iruka == 'y':
        print('コンビニのチキンはいかがですか')
else:
    print('家で食べましょう')
