import time
import threading

def sayHello():
    print("Hello world!")

def jobSchedule(f, n):
    time.sleep(n / 1000)
    t = threading.Thread(target=f)
    t.start()

jobSchedule(sayHello, 5000)