'''
'reverse inputpath outputpath'
'copy inputpath outputpath'
'duplicate-contents inputpath n'
'replace-string inputpath needle newstring'
arr[0]: main.py
arr[1]: command
arr[2:]: other
'''
from action import actSome
import sys
arr = sys.argv
actSome(arr)
