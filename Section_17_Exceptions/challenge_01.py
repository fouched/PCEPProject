
try:
    gateway = 'Gateway: Opened'
    print(gateway)
    x = '2' + 2
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    gateway = 'Gateway: Closed'
    print(gateway)
