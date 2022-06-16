
def factorial(x):
    if x == 1:
        print('You passed in: 1')
        return 1
    else:
        print(x)
        return x * factorial(x-1)


factorial_number = factorial(5)
print(factorial_number)
