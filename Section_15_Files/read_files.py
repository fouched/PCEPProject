"""
Files
"""

f = open('text.txt', 'r')
print(f.read())
# must close file
f.close()

print('--- using context manager ---')
# better way using context manager, will open and close file
with open('text.txt', 'r') as f:
    # print(f.read())

    # print(f.readline())

    # for line in f:
    #     print(line)

    # read arbitrary amount of chars
    print(f.read(40))

