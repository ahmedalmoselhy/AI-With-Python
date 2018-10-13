class queue:
    L = []
    def __init__(self):
        print(self.L)
    def enqueue(self,element):
        self.L.append(element)
    def dequeue(self):
        if(self.isEmpty() == False):
            return self.L.pop(0)
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0


Q1 = queue()
Q1.enqueue(10)
Q1.enqueue(20)
Q1.enqueue(30)
Q1.enqueue(40)
Q1.enqueue(50)

print (Q1.count())
print(Q1.isEmpty())

Q1.dequeue()
Q1.dequeue()
Q1.dequeue()
Q1.dequeue()
Q1.dequeue()
Q1.dequeue()
Q1.dequeue()