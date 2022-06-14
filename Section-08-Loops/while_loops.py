"""
While loops
"""
x = 0

while x < 10:
    x+= 1
    print(x)
    # skip 6
    if x == 6:
        continue

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print('x is larger than 10')

# Modulo
i = 10
while i <= 10 and i > 5:
    if i % 2 == 0:
        print(f'{i} is divisible by 2')
    else:
        print(f'{i} is divisible not by 2')
    i -= 1

