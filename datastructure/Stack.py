

class Stack:

    def __init__(self):

        self.stack = [];
        
    def push(self,value):
        self.stack.append(value);

    def pop(self):

        data = self.stack[-1];
        del self.stack[-1];
        return data;

    def peek(self):
        return self.stack[-1];
    
    def is_empty(self):

        return self.stack ==[];

    
    def __str__(self):
        return ','.join(str(num) for num in self.stack);

        


    

stack = Stack();
stack.push(10);
stack.push(20);
stack.push(30);
stack.push(40);

print(stack.peek());
print(stack.pop());
print(stack);

