height = float(input('身長cm >>'))
weight = float(input('体重kg >>'))
bmi = weight / (height/100 * height/100)
print(f'BMIは{bmi:.2f}です')
