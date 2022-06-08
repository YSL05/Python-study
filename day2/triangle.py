"""
绘制三角形
Version : 0.1
Author  : YSL
Date    : 2019-10-11
"""

line = int(input('please input line: '))
for i in range(1,line + 1):
    for j in range(1,i + 1):
        print('*', end='')
    print()

for i in range(1,line + 1):
    for j in range(1,line - i + 1):
        print(' ',end='')
    for j in range(line - i + 1,line + 1):
        print('*',end='')
    print()

for i in range(1,line + 1):
    for j in range(1,line - i + 1):
        print(' ',end='')
    for j in range(1,2 * i):
        print('*',end='')
    print()


        