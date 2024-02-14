class Node:

    def __init__(self,data):
        self.data = data;
        self.nextNode = None;

class List:

    def __init__(self):
        self.size = 0;
        self.head = None;
        self.tail = None;


    def add(self,value):

        new_node = Node(value);

        if self.head is None:
            self.head = new_node;
            self.tail = self.head;
        else:
            self.tail.nextNode = new_node;
            self.tail = new_node;


    def add_first(self,data):
        new_node = Node(data);
        
        if self.head is not None:
            new_node.nextNode = self.head;
            self.head = new_node;
        else:
            self.head = new_node;

    def add_at(self,data,position):
        new_node = Node(data);
        if position == 0:
            self.add_first(data);
            return True;
        else:
            self.tmp = self.head;
            for index in range(position-2):
                self.tmp = self.tmp.nextNode;

            new_node.nextNode = self.tmp.nextNode;
            self.tmp.nextNode = new_node;
            return True;


    def remove_first(self):
        
        current = self.head;
        current = current.nextNode;
        self.head = current;

    def remove_at(self,position):
        if position == 1:
            self.remove_first();
        current = self.head;

        for index in range(position-2):
            current = current.nextNode;
        current.nextNode = current.nextNode.nextNode;


    def search(self,data):
        current = self.head;
        while current is not None:
            if current.data == data:
                return True;
            current = current.nextNode;
        return False;
        

    def print_node(self):

        current = self.head;
        while current is not None:
            print(current.data);
            current = current.nextNode;


    def __str__(self):
        result_list = [];
        current = self.head;
        while current is not None:
            result_list.append(current.data);
            current = current.nextNode;
        result = ','.join(str(num) for num in result_list);
        return result;


list = List();
list.add(1);
list.add(3);
list.add(5);
#list.add_first(0);
list.add_at(2,2);
list.add_at(4,4);
list.add(6);
list.add_at(0,0);
#list.remove_first();
list.remove_at(1);
list.print_node();
print(list);
print(list.search(0));
