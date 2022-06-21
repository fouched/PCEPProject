"""
Functions 2!
"""


def my_function(*bunch_of_data):
    print(bunch_of_data[-1])


def my_function_2(high, low):
    print(high)
    print(low)


def my_function_3(country = 'South Africa'):
    print(country)


def multiply(no_one, no_two):
    return no_one * no_two


my_function(1, 2, 3, 4, 5, 'a')

# swap args by specifying them
my_function_2(low=8, high=10)

my_function_3('Sweden')
my_function_3('India')
my_function_3()

sum_total = multiply(2, 5)
print(sum_total)

