
class Node:

    def __init__(self,value=None):
        self.value = value;
        self.next = None;


class List:

    def __init__(self):
        self.head = None;
        self.tail = None;

    def add(self,value):

        node = Node(value);
        if self.head == None:
            self.head = node;
            self.tail = node;
        else:
            self.tail.next = node;
            self.tail = node;

    def __iter__(self):# it is special method it will call automatically 
        node = self.head;
        while node:#as long as node is True
            yield node;# it generator[It yields the current node object back to the caller]
            node = node.next;

    def print_node(self):

        current = self.head;
        while current !=None:
            print(current.value);
            current = current.next;



lists = List();
lists.add(10);
lists.add(20);
lists.add(30);
lists.add(40);
lists.add(50);
#print(lists.head.value);
#lists.print_node();
#print(lists.tail.next);

for node in lists:
    print(node.value);

#print([node.value for node in lists]);




'''node1 = Node(10);
node2 = Node(20);
node3 = Node(30);

singlyList.head = node1;
singlyList.head.next = node2;
singlyList.tail = node2;'''


