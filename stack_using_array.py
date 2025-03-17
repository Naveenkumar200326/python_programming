class stacklist:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        self.stack.pop()
    def display(self):
        print(self.stack)
    def peek(self):
        print(self.stack[-1])
    def size(self):
        print(len(self.stack))
    def isempty(self):
        x=len(self.stack)
        if(x==0):
            print("True")
        else:
            print("False")
s=stacklist()
s.push(90)
s.push(80)
s.push(70)
s.display()
s.size()
s.isempty()
s.peek()
s.pop()
s.display()
