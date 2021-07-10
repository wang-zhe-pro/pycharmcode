import threading
import time
import sys
def job1():
    global A

    for i in range(10):
        lock.acquire()
        A+=1

        print('job1',A)
        lock.release()
        # time.sleep(1)


def job2():
    global A
    for i in range(10):
        lock.acquire()
        A+=10
        print('job2',A)
        lock.release()
        # time.sleep(1)



if __name__ == "__main__":
    A=0
    lock=threading.Lock()
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.run()
    t2.run()



