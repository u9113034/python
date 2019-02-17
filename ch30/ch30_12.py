# ch30_12.py
import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')
def manager():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

m = threading.Thread(name='Manager', target=manager)
w = threading.Thread(name='worker1', target=worker)
w2 = threading.Thread(name='worker2',target=worker)
m.start()
w.start()
w2.start()



