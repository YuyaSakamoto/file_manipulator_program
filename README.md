## Title
File Manipulator Program
## Memo
1.ファイルの読み書きとシェルの引数入力の取り方を学ぶために'file_manipular'を作成する

2.CLI'main.py [command] [option] [option]'と入力すれば動く

3.バリデータの入力もしてあります。

4.classの代わりにファイルで分けて管理してあります。
## file_manipulatorについて
- 'reverse inputpath outputpath'
inputpathにあるファイルを受取、outputpathにinputpathの内容を逆にした新しいファイルを作成します。
- 'copy inputpath outputpath'
inputpathにあるファイルのコピーを作成し、outputpathとして保存します
- 'duplicate-contents inputpath n'
inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにn回複製します。
- 'replace-string inputpath needle newstring'
inputpathにあるファイルの内容から文字列'needle'を検索し、'needle'の全てを'newstring'に置き換えます。
