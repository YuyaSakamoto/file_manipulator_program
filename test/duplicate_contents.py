'''
'duplicate-contents inputpath n'
inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回複製します。
'''
import sys
arr = sys.argv
print("スクリプト名: " + arr[0])
print("command: " + arr[1])
print("inputPath: " + arr[2])
print("outputPath: " + arr[3])
content = ""
s = ""
if arr[1] == "duplicate":
    content = ""
    with open(arr[2], "r") as f:
        s += f.read()
        for _ in range(int(arr[3])):
            content += s + '\n'
        print(content[:-1])

    with open(arr[2], "w") as f:
        f.write(content[:-1])