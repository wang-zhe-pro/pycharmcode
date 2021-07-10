import threading
import sys
import time
import pdb


def showfoo(n):
    for _ in range(n):
        lockpython.acquire()  # 获取对方的锁，释放自己的锁
        print('foo',end="")
        sys.stdout.flush()  # 释放缓冲区

        lockfoo.release()
        time.sleep(1)


def showbar(n):
    for _ in range(n):
        lockfoo.acquire()  # 获取对方的锁，释放自己的锁
        print('bar',end="")
        sys.stdout.flush()  # 释放缓冲区
        lockbar.release()
        time.sleep(1)
def showpython(n):
    for _ in range(n):
        lockbar.acquire()  # 获取对方的锁，释放自己的锁
        print('python',end="")
        sys.stdout.flush()  # 释放缓冲区
        lockpython.release()
        time.sleep(1)

if __name__ == '__main__':
    lockfoo = threading.Lock()  # 定义3个互斥锁
    lockbar = threading.Lock()
    lockpython = threading.Lock()
    n = int(input())
    t1 = threading.Thread(target=showfoo, args=[n])  # 定义3个线程
    t2 = threading.Thread(target=showbar, args=[n])
    t3 = threading.Thread(target=showpython, args=[n])
    lockfoo.acquire()  # 先锁住foo,bar锁，保证先打印foo
    lockbar.acquire()

    t1.start()
    t2.start()
    t3.start()




