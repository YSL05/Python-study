"""
hunder money hunder chicken
Version : 0.1
Author  : YSL
"""

for i in range(0,21):
    for j in range(0,30):
        for k in range(0,30):
            if i + j + 3 * k == 100:
                if 5 * i + 3 * j + k == 100:
                    print('there are %d cork、%d hen、%d chick' %(i,j,3 * k))
                    
