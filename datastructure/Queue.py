
class Queue:

    def __init__(self):

        self.queue = [];

    def is_empty(self):
        return self.queue == [];

    def enque(self,value):

        self.queue.append(value);

    def dqueue(self):
        data = self.queue[0];
        del self.queue[0];
        return data;

    def peek(self):
        return self.queue[0];

    def size(self):
        return len(self.queue);

    def __str__(self):

        return ','.join(str(num) for num in self.queue);


queue = Queue();
queue.enque(10);
queue.enque(20);
queue.enque(30);
queue.enque(40);

print(queue.is_empty());
print(queue.peek());
print(queue.dqueue());
print(queue);
