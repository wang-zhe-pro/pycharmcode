import random
import threading
from time import sleep
import numpy as np

index = [99, 37, 57, 85, 83, 1, 25, 22, 58, 97, 40, 18, 38, 82, 63, 98, 27, 80, 88, 17]

def sleep_sort(i):
    sleep(i*0.1)
    print(i)
[threading.Thread(target=sleep_sort, args=(i,)).start() for i in index]
