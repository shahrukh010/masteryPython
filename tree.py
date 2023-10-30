
class Node:

    def __init__(self,data):
        self.data = data;
        self.leftchild = None;
        self.rightchild = None;
        self.preitems = [];
        self.initems = [];
        self.postitems = [];


    def preorder(self,current_node):

            if current_node:
                #print(current_node.data)
                self.preitems.append(current_node.data);
                self.preorder(current_node.leftchild);
                self.preorder(current_node.rightchild);

    def inorder(self,current_node):
        if current_node:
            self.inorder(current_node.leftchild);
            self.initems.append(current_node.data);
            self.inorder(current_node.rightchild);

    def postorder(self,current_node):
        if current_node:

            self.postorder(current_node.leftchild);
            self.postorder(current_node.rightchild);
            self.postitems.append(current_node.data);

    def itr_preorder(self,current_node):
        
        stack = [];
        while current_node or len(stack) !=0:
            if current_node:
                stack.append(current_node);
                self.preitems.append(current_node.data);
                #print(current_node.data);
                current_node = current_node.leftchild;
            else:
                current_node = stack.pop();
                current_node = current_node.rightchild;

    def itr_inorder(self,current_node):

        stack = [];
        while current_node or len(stack) !=0:

            if current_node:
                stack.append(current_node);
                current_node = current_node.leftchild;
            else:
                current_node = stack.pop();
                #print(current_node.data);
                self.initems.append(current_node.data);
                current_node = current_node.rightchild;

    def itr_postorder(self,current_node):

        stack = [];
        stack.append(current_node);
        postdata = [];

        while stack:

            tmp = stack.pop();
            postdata.append(tmp);

            if tmp.leftchild:
                stack.append(tmp.leftchild);

            if tmp.rightchild:
                stack.append(tmp.rightchild);

        for data in postdata:
            self.postitems.append(data.data);
        self.postitems.reverse();


    def itr_level_order(self,current_node):

        s1 = [];
        s2 = [];
        s1.append(current_node);

        while s1:
            tmp = s1.pop();
            s2.append(tmp);

            if tmp.leftchild:
                s1.append(tmp.leftchild);
            if tmp.rightchild:
                s1.append(tmp.rightchild);

        while s2:
            data = s2.pop().data;
            print(data,end=",")






node = Node(10);
node.leftchild = Node(8);
node.rightchild = Node(12);
node.leftchild.leftchild = Node(7);
node.rightchild.rightchild = Node(18);
node.leftchild.rightchild = Node(9)
node.rightchild.leftchild = Node(11);

node.preorder(node);
print('preorder:',node.preitems);

node.inorder(node);
print('inorder:',node.initems);

node.postorder(node);
print('postorder:',node.postitems);

node.preitems.clear();
node.itr_preorder(node);
print('pre_order_itr_version',node.preitems);

node.initems.clear();
node.itr_inorder(node);
print('in_order_itr_version',node.initems);

node.postitems.clear();
node.itr_postorder(node);
print('post_order_itr_version',node.postitems);

node.itr_level_order(node);


