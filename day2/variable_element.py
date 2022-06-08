"""
输入三边长，计算三角形的面积和周长
Version : 0.1
Author  : YSL 
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + b > c and a + c >b:
    print('perimeter: %.2f' %(a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('area: %.2f' % area)
else:
    print('please input valid parameter')