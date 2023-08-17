height = int(input('何段の階段を作る? >>'))
for n in range(1, height+1):
    print('*' * n)

"""
for i in range(height):
    for j in range(i + 1):
        print('*', end="")
"""
