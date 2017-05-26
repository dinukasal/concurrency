# -*- coding: utf-8 -*-
"""
Created on Wed May 24 21:26:28 2017

@author: dinuka
"""

import threading
import time

def thread1(s1,s2):
    for i in range(5):
        #s1.acquire()
        try:
            print 'A',
        finally:
            s1.acquire()
            s2.release()
        time.sleep(0.1)
        
def thread2(s1,s2):
    for i in range(5):
        s1.release()        
        s2.acquire()
        s1.release()
        try:
            print 'B',
        finally:
            s2.acquire()
        time.sleep(0.1)

s1 = threading.Semaphore(1)
s2 = threading.Semaphore(1)
#lock = threading.Lock()
w = threading.Thread(target=thread1, args=(s1,s2,))
nw = threading.Thread(target=thread2, args=(s1,s2,))

w.start()
nw.start()