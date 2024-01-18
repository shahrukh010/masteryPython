class Node(object):

    def __init__(self,data):
        self.data = data;
        self.nextNode = None;


class LinkedList(object):

    def __init__(self):
        self.size = 0;
        self.head = None;

    def add_first(self,data):

        newNode = Node(data);

        if self.head is None:
            self.head = newNode;
        else:
            self.nextNode = newNode;
            self.head = newNode;



    def add(self,data):

        self.size = self.size+1;
        newNode = Node(data);

        if not self.head:
            self.head = newNode;
        else:
            current = self.head;
            while current.nextNode: 
                current = current.nextNode;
            current.nextNode = newNode;



    def get_size(self):
        actualNode = self.head;
        size = 0;

        while actualNode is not None:
            size = size+1;
            actualNode = actualNode.nextNode;

        return size;

    def print(self):
        current = self.head;
        while current is not None:
            print(current.data);
            current = current.nextNode;

list = LinkedList();
list.add_first(5);
list.add(10);
list.add(20);
list.add(30);
list.print();
print(list.get_size());
