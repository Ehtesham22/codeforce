from collections import deque

class queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]

    def size(self):
        return len(self.queue)
    

if __name__ == '__main__':
    q1 = queue()
    q2 = queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    # print(q1.dequeue())
    # print(q1.queue)
   
    # print(q2.queue)
    for i in range(len(q1.queue)):
        q2.enqueue(q1.dequeue())
    print(q2.queue)




    