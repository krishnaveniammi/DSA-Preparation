from collections import deque
import threading
import time

class  Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self,item):
        self.queue.appendleft(item)
    def dequeue(self):
        return self.queue.pop()
    def is_empty(self):
        return len(self.queue) == 0
q = Queue()

def placing_order(orders):
    for order in orders:
        q.enqueue(order)
        time.sleep(0.5)
def serving_order():
    while not q.is_empty():
        print("Serving order:",q.dequeue()) 
        time.sleep()
orders = ['pizza','burger','pasta','samosa','biryani']
t1 = threading.Thread(target=placing_order,args=(orders,))
t2 = threading.Thread(target=serving_order)
t1.start()
t2.start()

        
    
    