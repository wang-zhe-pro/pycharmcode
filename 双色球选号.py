from random import randrange, randint, sample
import random


def display(balls):
    """
    按照题目所要求格式输出列表中的双色球号码

    :param balls:双色球号码列表，如[9,12,16,20,30,33 3]
    :print:输出格式为09 12 16 20 30 33 | 03
    :return: 无返回值

    """
    #        请在此处添加代码       #
    # *************begin************#
    s = []
    for i in balls:
        if (i % 10 == i):
            s.append(str(i).zfill(2))
        else:
            s.append(str(i))
    for i in range(len(s)-1):
        print(s[i],end=" ")
    print("|",end=" ")
    print(s[-1],end=" ")
    print()
    # **************end*************#


def random_select():
    """
    随机选择一组号码
    :return: 返回随机选择的这一组号码，如[9,12,16,20,30,33 3]
    """
    #        请在此处添加代码       #
    # *************begin************#
    red=[x for x in range(1,34)]
    bule=[x for x in range(1,17)]
    red_ball=sample(red,6)
    bule_ball=sample(bule,1)
    red_ball.sort();
    red_ball.append(bule_ball[0])
    return  red_ball
    # **************end*************#


# n为注数
def main(n):
    for _ in range(n):
        display(random_select())


random.seed(3)
n = int(input())
if __name__ == '__main__':
    main(n)


