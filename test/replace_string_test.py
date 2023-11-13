'''
'replace-string inputpath needle newstring'
inputpathにあるファイルの内容から文字列'needle'を検索し、
'needle'の全てを'newstring'に置き換えます。
'''
import sys
arr = sys.argv
print("スクリプト名: " + arr[0])
print("command: " + arr[1])
print("inputPath: " + arr[2])
print("needle: " + arr[3])
print("new string: " + arr[4])
content = ""
if arr[1] == "replace":
    content = ""
    with open(arr[2], "r") as f:
        content += f.read()
        print(content)
        content = content.replace(arr[3], arr[4])
        print(content)

    with open(arr[2], "w") as f:
        f.write(content)