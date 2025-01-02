class Queue(list):
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data):
        self.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("Queue is UnderFlow")
        
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue is UnderFlow")
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue is UnderFlow")
    def size(self):
        return len(self)
    

q1 = Queue()

try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front ==> ", q1.get_front(), "Rear ==> ", q1.get_rear())

try:
    q1.dequeue()
    print("Queue has now ", q1.size(), "elements")
except IndexError as e:
    print(e.args[0])