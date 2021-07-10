import threading
from multiprocessing import  Pool
import time
import sys
import time

def a():

    for _ in range(4):



        print('a')
        sys.stdout.flush()
        time.sleep(0.2)





def b():

    for _ in range(4):



        print('b')
        sys.stdout.flush()

        time.sleep(0.2)




if __name__ == "__main__":

    p=Pool(2)
    p.apply_async(a)
    p.apply_async(b)
    p.close()
    p.join()


