def reverse(inputPath, outputPath):
    print('inputPath :', inputPath)
    print('outputPath :', outputPath)
    content = ""
    with open(inputPath, "r") as f:
        lines = f.read()
        content += lines[::-1]
        print(content)

    with open(outputPath, "w") as f:
        f.write(content)

def copy(inputPath, outputPath):
    print('inputPath :', inputPath)
    print('outputPath :', outputPath)
    content = ""
    with open(inputPath, "r") as f:
        content += f.read()
        print(content)

    with open(outputPath, "w") as f:
        f.write(content)

def duplicate_contents(inputPath, num):
    content = ""
    with open(inputPath, "r") as f:
        s += f.read()
        for _ in range(int(num)):
            content += s + '\n'
        print(content[:-1])

    with open(inputPath, "w") as f:
        f.write(content[:-1])

def replace_string(inputPath, needle, newString):
    content = ""
    with open(inputPath, "r") as f:
        content += f.read()
        print(content)
        content = content.replace(needle, newString)
        print(content)

    with open(inputPath, "w") as f:
        f.write(content)

def actSome(arr):
    print(arr)
    print("command :", arr[1])
    if arr[1] in ('reverse', '-rev'):
        print('reverse on')
        reverse(arr[2],arr[3])
    elif arr[1] in ('copy', '-c'):
        print('copy on')
        copy(arr[2],arr[3])
    elif arr[1] in ('duplicate', '-d'):
        print('duplicate-contents on')
        duplicate_contents(arr[2],arr[3])
    elif arr[1] in ('replace', '-rep'):
        print('replace-string on')
        replace_string(arr[2], arr[3], arr[4])
    else:
        print('not found')