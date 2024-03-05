
class TreeNode:

    def __init__(self,data,children = []):
        self.data = data;
        self.children = children;

    def addchild(self,node):
        self.children.append(node);

    def __str__(self,level = 0):
        ret = " " * level + str(self.data) +"\n"
        for child in self.children:
            ret += childhahrukh010/masteryPython.git__str__(level +1);
        return ret;


root = TreeNode('Drink');
cold = TreeNode("Cold");
hot = TreeNode("Hot");
root.addchild(cold);
root.addchild(hot);
print(root);

