
class Stack:

    def __init__(self):
        self.list = [];

    #string representation for object
    def __str__(self):
        values = self.list.copy();
        values.reverse();
        values = [str(x) for x in values];
        return '\n'.join(values);


    def isEmpty(self):
        if self.list == []:
            return True;
        else:
            return False;


    def push(self,value):
        self.list.append(value);

    def pop(self):
        
        if self.isEmpty():
            return False;
        else:
            self.list.pop();

    def peek(self):
        
        if self.isEmpty():
            return False;
        return self.list[len(self.list)-1];

stack = Stack();
print(stack.isEmpty());
stack.push(10);
stack.push(20);
stack.push(30);
stack.push(40);
stack.push(50);
print(stack);
print("After pop");
print(stack);
print(stack.peek());

