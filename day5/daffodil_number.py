"""
find the daffodil number
Version : 0.1
Author  : YSL
"""

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if 100 * i + 10 * j + k == i ** 3 + j ** 3 + k ** 3:
                print('daffodil number is %d' % int(100 * i + 10 * j + k))

