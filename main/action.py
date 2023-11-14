'''
'reverse inputpath outputpath'
'copy inputpath outputpath'
'duplicate-contents inputpath n'
'replace-string inputpath needle newstring'
arr[0]: main.py
arr[1]: command
arr[2:]: other
'''
def reverse(inputPath, outputPath):
    print('outputPath :', outputPath)
    try:
        content = ""
        with open(inputPath, "r") as f:
            lines = f.read()
            content += lines[::-1]
            print(content)

        with open(outputPath, "w") as f:
            f.write(content)
    except Exception as e:
        print(e)
        print(type(e))

def copy(inputPath, outputPath):
    print('outputPath :', outputPath)
    try:
        content = ""
        with open(inputPath, "r") as f:
            content += f.read()
            print(content)

        with open(outputPath, "w") as f:
            f.write(content)
    except Exception as e:
        print(e)
        print(type(e))

def duplicate_contents(inputPath, num):
    print("num :", num)
    try:
        num = int(num)
        content = ""
        with open(inputPath, "r") as f:
            s = f.read()
            for _ in range(int(num)):
                content += s + '\n'
            print(content[:-1])

        with open(inputPath, "w") as f:
            f.write(content[:-1])
    except Exception as e:
        print(e)
        print(type(e))

def replace_string(inputPath, needle, newString):
    print("needle :", needle)
    print("new string:", newString)
    try:
        content = ""
        with open(inputPath, "r") as f:
            content += f.read()
            print(content)
            content = content.replace(needle, newString)
            print(content)

        with open(inputPath, "w") as f:
            f.write(content)
    except Exception as e:
        print(e)
        print(type(e))

def actSome(arr):
    print(arr)
    print("command :", arr[0])
    print('inputPath :', arr[1])
    try:
        if arr[0] in ('reverse', '-rev'):
            print('reverse on')
            reverse(arr[1],arr[2])
        elif arr[0] in ('copy', '-c'):
            print('copy on')
            copy(arr[1],arr[2])
        elif arr[0] in ('duplicate', '-d'):
            print('duplicate-contents on')
            duplicate_contents(arr[1],arr[2])
        elif arr[0] in ('replace', '-rep'):
            print('replace-string on')
            replace_string(arr[1], arr[2], arr[3])
        else:
            print('not found')
    except Exception as e:
        print(e)
        print(type(e))