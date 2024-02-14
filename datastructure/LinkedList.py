
class Node:
    def __init__(self,data):
        self.data = data;
        self.nextNode = None;

class List:
    
    def __init__(self):
        self.head = None;
        self.first= None;
        self.tail = None;
        self.size = 0;

    def add_first(self,value):
        self.size = self.size+1;

        new_node = Node(value);

        if not self.head:
            self.head = new_node;
        else:
            new_node.nextNode = self.head;
            self.head = new_node;

    def add(self,value):
        self.size = self.size+1;
        new_node = Node(value);

        if not self.first:
            self.first = new_node;
            self.tail = self.first;
        else:
            self.tail.next = new_node;
            self.tail = new_node;

    def print_node(self):
        current = self.head;
        while current is not None:
            print(current.data);
            current = current.nextNode;



list = List();
#list.add_first(5);
#list.add_first(4);
#list.add_first(3);
#list.add_first(2);
#list.add_first(1);
#list.print_node();

list.add(1);
list.add(2);
list.add(3);
list.add(4);
print(list);
