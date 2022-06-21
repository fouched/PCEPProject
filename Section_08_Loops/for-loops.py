"""
For loops
"""

numbers = [1, 2, 3, 4, 5]

# the iterator (i) can be called anything
for i in numbers:
    print(i)

sum_of_loop = 0
print("-------------------------------")
for x in range(3, 6):
    sum_of_loop += x
    print(x)

print(sum_of_loop)

co_workers = ['Tom', 'Ben', 'Adil']
for x in co_workers:
    if x == 'Adil':
        break
    print(f'Hello {x}!')
