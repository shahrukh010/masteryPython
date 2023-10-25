
class Stack:

    def __init__(self):
        self.list = [];

    def __str__(self):
        values = self.list.reverse();
        values = [str(x) for x in self.list];
        return '\n'.join(values);

    def isEmpty(self):

        if self.list == []:
            return True;
        else:
            return False

    def push(self,data):
        self.list.append(data);
        return True;

    def pop(self):

        if self.list == []:
            return 'There is not element'
        else:
            self.list.pop();

    def peek(self):

        if self.list == []:
            return 'There is not element'
        else:
            return self.list[len(self.list)-1]


stack = Stack();
print(stack.isEmpty());        
stack.push(10);
stack.push(20);
stack.push(30);
#stack.pop();
print(stack.peek());
print(stack);
