class Queue:
    def __init__(self):
        self.q = list()
    def enqueue(self,data):
        self.q.append(data)
    def dequeue(self,data):
        self.q.pop()
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)

