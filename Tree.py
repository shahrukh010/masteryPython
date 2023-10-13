
class TreeNode:

    def __init__(self,data,children=[]):
        self.data = data;
        self.children = children;


    def __str__(self,level = 0):

        res = " " * level + str(self.data) + "\n";
        for child in self.children:
            res +=child.__str__(level + 1)
        return res;

    def addChild(self,node):
        self.children.append(node);


treeNode = TreeNode('Drink',[]);
cold = TreeNode('Cold',[]);
hot = TreeNode('Hot',[]);
treeNode.addChild(cold);
treeNode.addChild(hot);
print(treeNode);
