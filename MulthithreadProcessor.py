'''
Created on 16-Nov-2015

@author: Virendra
'''
from concurrent.futures.thread import ThreadPoolExecutor
import threading
import time

def square(n):
    print ("Calculating square of %d by thread name %s " % (n, threading.current_thread()))
    time.sleep(3)
    print ("Square of number %d is %d calculated by thread %s " % (n, n*n, threading.current_thread()))

executor = ThreadPoolExecutor(max_workers=5)
numbers = range(1,10)
for number in numbers:
    executor.submit(square, number)