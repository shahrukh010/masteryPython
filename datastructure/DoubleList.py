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
    def __str__(self):

        list_result = [];
        current = self.first;
        while current is not None:
            list_result.append(current.data);
            current = current.next;
        result = ','.join(str(num) for num in list_result);
        return result;



class CList:

    def __init__(self):
        self.first = None;
        self.last = None;

    def add(self,value):

        new_node = Node(value);

        if self.first is None:
            self.first = new_node;
            self.last = self.first;
        else:
            self.last.next = new_node;
            self.last = new_node;
            self.next = self.first;

    def print_node(self):

        head = self.first;
        current = self.first.next;
        print(head.data);
        while current is not None and current.data !=head.data:
            print(current.data);
            current = current.next;
        



list = List();
list.add(10);
list.add(20);
list.add(30);
list.add(40);
list.add(50);
list.add(60);
#list.print_node();
#print(list);

c = CList();
c.add(100);
c.add(200);
c.add(300);
c.add(400);
c.add(500);
c.print_node();


