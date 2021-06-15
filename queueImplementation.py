# A queue implementation

queue = []

def enqueue(x):
    queue.append(x)
    print(f"Enqueuing {x}")
    print(queue)

def dequeuee():
    if (len(queue) == 0):
        print("Queue is empty")
    else:
        print(f"Dequeued first element {queue[0]}")
        queue.pop(0)
    
    print(queue)

enqueue(1)
enqueue(2)
enqueue(3)
dequeuee()
dequeuee()

from collections import deque
x = [7,8,9,10]
queue2 = deque(x)
print(queue2)
queue2.popleft()
print(queue2)
