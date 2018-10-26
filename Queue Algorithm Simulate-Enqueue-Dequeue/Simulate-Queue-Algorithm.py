class queue:
    # This is a class to simulate Queue Algorithm
    L = []
    def __init__(self):
        # The Constructor
        print(self.L)
    def enqueue(self,element):
        # Adding elements to the queue
        self.L.append(element)
    def dequeue(self):
        # Removing elements from the queue
        if(self.isEmpty() == False):
            return self.L.pop(0)
        else:
            return None
    def count(self):
        # counting the queue elements
        return len(self.L)
    def isEmpty(self):
        # check if queue is empty
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