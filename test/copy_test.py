'''
'copy inputpath outputpath'
inputpathにあるファイルのコピーを作成し、outputpathとして保存します
'''
import sys
arr = sys.argv
print("スクリプト名: " + arr[0])
print("command: " + arr[1])
print("inputPath: " + arr[2])
print("outputPath: " + arr[3])
content = ""
if arr[1] == "copy":
    content = ""
    with open(arr[2], "r") as f:
        content += f.read()
        print(content)

    with open(arr[3], "w") as f:
        f.write(content)