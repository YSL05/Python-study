"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: YSL
Date: 2019-10-11
"""

from math import sqrt

num = int(input('please input positive integer: '))
end = int(sqrt(num))
is_prime = True
for i in range(2,end + 1):
    if num % i == 0:
        is_prime = False
    break
if is_prime and num != 1:
    print('%d is prime' % num)
else:
    print('%d is not prime' % num)  