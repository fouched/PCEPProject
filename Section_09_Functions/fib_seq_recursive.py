def fib_seq(amount):
    if amount == 0:
        return 0
    elif amount == 1:
        return 1
    else:
        return fib_seq(amount - 2) + fib_seq(amount - 1)


for x in range(13):
    print(fib_seq(x))
