class Node:

    def __init__(self,data):
        self.data = data;
        self.next = None;
        self.prev = None;


class List:

    def __init__(self):
        self.size = 0;
        self.first = None;
        self.tail = None;

    def add(self,value):
        self.size = self.size+1;

        new_node = Node(value);

        if self.first is None:
            self.first = new_node;
            self.tail = self.first;
        else:
            self.tail.next = new_node;
            new_node.prev = self.tail;
            self.tail = new_node;

    def print_node(self):

        first_current = self.first;
        tail_current = self.tail;
        
        while first_current and tail_current is not None:
            
            if first_current:
                print(f'First Current: {first_current.data}',end='\t');
                first_current = first_current.next;
            else:
                print('\t',end='');

            if tail_current:
                print(f'Tail Current: {tail_current.data}');
                tail_current = tail_current.prev;
            else:
                print('');



list = List();
list.add(10);
list.add(20);
list.add(30);
list.add(40);
list.add(50);
list.add(60);
list.print_node();

