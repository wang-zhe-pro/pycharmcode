import math
from multiprocessing import cpu_count
from multiprocessing import Pool
import time


def isPrime(n):


# 判断数字是否为素数
#        请在此处添加代码       #
# *************begin************#
    if n>1:
        for num in range(2,(int)(math.sqrt(n)+1)):
            if(n%num==0):
                return False
        else:
            return True
    else:
        return False

# **************end*************#


def howMany(T):


# 计算给定区间含有多少个素数
#        请在此处添加代码       #
# *************begin************#
    num=0

    for i in range((int)(T[0]),(int)(T[1])+1):
        if(isPrime(i)):
            num=num+1

    return  num
# **************end*************#


def separateNum(N, CPU_COUNT):


# 对整个数字空间N进行分段CPU_COUNT
#        请在此处添加代码       #
# *************begin************#
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)]
            for i in range(0, CPU_COUNT)]
    list[0][0] = 1

    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    print(list)
    return list


# **************end*************#

if __name__ == '__main__':

    N = int(input())
    # 多进程
    CPU_COUNT = 12  ##CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList = separateNum(N, CPU_COUNT)
    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(howMany, (sepList[i],)))
    pool.close()
    pool.join()
    # ans = 0
    list = [res.get() for res in result]
    print(sum(list))




