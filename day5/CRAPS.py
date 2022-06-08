"""
CRAPS
the player have 1000 at the beginning, when you lose total the game is over 
Version : 0.1
Author  : YSL
"""

from random import randint
money = 1000
counter = 0
print('玩家面前有两个色子，玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。')
print('游戏规则如下：1、资产为负游戏结束。2、必须下注7次才能离开游戏。3、加注不能少于100')
while money > 0:
    counter = counter + 1
    if counter >=2:
        clear_screen = int(input('按0清除此前的游戏记录,按其他数字继续游戏'))
        if clear_screen == 0:
            import os
            i=os.system("cls")
            print('玩家面前有两个色子，玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。')
            print('游戏规则如下：1、资产为负游戏结束。2、必须下注7次才能离开游戏。3、加注不能少于100')
    print('你的总资产为：%d' % money)
    if counter > 7:
        end = int(input('按2可离开游戏，按其他数字继续游戏'))
        counter = 0
        if end == 2:
            print('恭喜你喜提%d' % money)
            break
    print('第%d局游戏开始' % counter)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break 
    while True:
        begin = int(input('按1摇色子'))
        if begin == 1:
            break 
    dice_fir = randint(1,6)
    dice_sed = randint(1,6)
    first = dice_fir + dice_sed
    print('其中一个色子的点数为%d' % dice_fir)
    while True:
        print('总资产为%d,下注为%d,还可加注%d' %(money,debt,money - debt))
        add_debt = int(input('是否加注：(0 or 其他数字 不能超过总资产)'))
        if add_debt >=100 or add_debt == 0:
            if 0 < add_debt + debt <= money:
                break 
    debt = debt + add_debt
    print('色子的点数为%d' % first)
    if first == 7 or first == 11:
        print('玩家赢')
        money = money + debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家赢')
        money = money - debt
    else:
        needs_go_on = True
    if needs_go_on:
        print('玩家和庄家都未获胜，进入循环局，此时下注为%d' % debt)
    while needs_go_on:
        needs_go_on = False
        dice_fir = randint(1,6)
        dice_sed = randint(1,6)
        current = dice_fir + dice_sed
        print('第一次摇的点数为%d   这次其中一个色子的数目为%d' % (first,dice_fir))
        while True:
            print('总资产为%d,下注为%d,还可加注%d' %(money,debt,money - debt))
            add_debt = int(input('是否加注：(0 or 其他数字)'))
            if add_debt >=100 or add_debt == 0:
                if 0 < add_debt + debt <= money:
                    break 
        print('玩家摇出了%d点' % current)
        debt = debt + add_debt
        if current == 7:
            print('庄家赢')
            money = money - debt
        elif current == first:
            print('玩家赢')
            money = money + debt
        else:
            needs_go_on = True
            print('玩家和庄家都未获胜，继续摇色子')

print('你破产了，游戏结束！')
