"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: YSL
"""

import random

answer  = random.randint(1,100)
counter = 0
while True:
    counter = counter + 1
    number = int(input('please input number: '))
    if number > answer:
        print('smaller')
    elif number < answer:
        print('bigger')
    else:
        print('you are right')
        break
print('total counters: %d' % counter)
if counter > 7:
    print('you are stupid')
    
            
