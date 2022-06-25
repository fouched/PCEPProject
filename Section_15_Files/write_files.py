"""
Files
"""

with open('text2.txt', 'w') as f:
    # f.write('This is a new file and some text')
    # if the file already exists it will overwrite current text
    f.write('Changing text')


with open('text.txt', 'r') as read_file:
    with open('text2.txt', 'w') as write_file:
        write_file.write(read_file.read())

# reading a photo, rb (read binary) must be used
with open('IMG_1489.JPG', 'rb') as f:
    print(f.read())

# write a photo - note the wb (write binary)
with open('IMG_1489.JPG', 'rb') as read_file:
    with open('IMG_2.jpg', 'wb') as write_file:
        write_file.write(read_file.read())
