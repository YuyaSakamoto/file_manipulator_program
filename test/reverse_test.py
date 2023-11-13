"""
'reverse_test.py reverse inputpath outputpath'
inputpathにあるファイルを受取、
outputpathにinputpathの内容を逆にした新しいファイルを作成します。
と入力してその結果を出せるようにしたい
"""
import sys
arr = sys.argv
print("スクリプト名: " + arr[0])
print("command: " + arr[1])
print("inputPath: " + arr[2])
print("outputPath: " + arr[3])
content = ""
if arr[1] == "reverse":
    with open(arr[2], "r") as f:
        lines = f.read()
        content += lines[::-1]
        print(content)

    with open(arr[3], "w") as f:
        f.write(content)