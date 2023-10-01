
class Node:
    
    def __init__(self,value=None):
        self.value = value;
        self.next = None;


class List:

    def __init__(self):
        self.head = None;
        self.tail = None;


    def add(self,value):
        new_node = Node(value);
        if self.head == None:
            self.head = new_node;
            self.tail = new_node;
        else:
            self.tail.next = new_node;
            self.tail = new_node;


    def add_node(self,value,location):
        new_node = Node(value);
        if location == 0:
            new_node.next = self.head;
            self.head = new_node;
            self.last = new_node;
        elif location == 1:
            tmp = self.head.next;
            new_node.next = tmp;
            self.head.next = new_node;
        else:
            tmp_node = self.head;
            index = 0;
            while index < location-1:
                tmp_node = tmp_node.next;
                index +=1;
            next_node = tmp_node.next;
            new_node.next = next_node;
            tmp_node.next = new_node;


    def traverse(self):
        if self.head is None:
            print('head is null');
        else:
            current_node = self.head;
            while current_node is not None:
                print(current_node.value);
                current_node = current_node.next;
        


    def __iter__(self):
        current = self.head;
        while current:
            yield current;
            current = current.next;


singly = List();
singly.add(10);
singly.add(20);
singly.add(30);
singly.add(40);
singly.add(50);
'''singly.add_node(5,0);
singly.add_node(7,1);
singly.add_node(0,0);
singly.add_node(3,1);
singly.add_node(9,2);
singly.add_node(26,6);'''

print([node.value for node in singly]);
singly.add_node(25,2);
singly.add_node(45,5);
singly.add_node(0,0);
singly.add_node(2,1);
singly.add_node(60,9);

print([node.value for node in singly]);
singly.traverse();





