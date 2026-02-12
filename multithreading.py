import threading
import time

def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
 
#normal code    
func(4)
func(6)    

#same code using threads
t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[6])

t1.start()
t2.start()


