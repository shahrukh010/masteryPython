
class Node:
    
    def __init__(self,data):
        self.data = data;
        self.leftchild = None;
        self.rightchild = None;


    def in_order(self,current_node):

        if current_node:
            print(current_node.data);
            self.in_order(current_node.leftchild);
            self.in_order(current_node.rightchild);

node = Node(10);
node.leftchild = Node(8);
node.leftchild.leftchild = Node(7);
node.rightchild = Node(12);
node.rightchild.rightchild = Node(15);
node.leftchild.rightchild = Node(9);
node.leftchild.leftchild.rightchild = Node(8);

node.rightchild.leftchild = Node(6);
node.rightchild.rightchild.leftchild = Node(5);
node.in_order(node);

node = Node(8);
node.in_order(node);




