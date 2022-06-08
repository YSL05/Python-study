"""
reverse_integer
Version : 0.1
Author  : YSL
"""

integer = int(input('please input integer : '))
reverse_integer = 0
while integer > 0:
    reverse_integer = reverse_integer * 10 + integer % 10
    integer = integer // 10
print('reverse_integer is %d' % reverse_integer)