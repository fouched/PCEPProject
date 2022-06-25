"""
Create a new file and print it
"""

with open('challenge.txt', 'w') as f:
    f.write('Some text for the file')

with open('challenge.txt', 'r') as f:
    print(f.read())
    