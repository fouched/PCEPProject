"""
Errors & Exceptions
"""

try:
    x = 10 * (1/0)
    print(x)
except ZeroDivisionError as e:
    print(f'{e} : Cannot devide by zero')

try:
    x = '2' + 2
    print(x)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('Will always run')

try:
    x = None
    if x is None:
        raise Exception('Error x cannot be None')
except Exception as e:
    print(e)

