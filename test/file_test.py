pathname = 'test.txt'
contents = ''

with open(pathname, 'w') as f:
    f.write(contents + "\Appending more text to this file!")

with open(pathname) as f:
    contents = f.read()
    print(contents)