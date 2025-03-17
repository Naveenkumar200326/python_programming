class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
        
    def pop(self):
        self.head=self.head.next
    
    def peek(self):
        print(self.head.data)
       
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print(" ")
        
    def isempty(self):
        count=0
        temp=self.head
        while temp!=None:
            temp=temp.next
            count=+1
        if(count==0):
            print(True)
        else:
            print(False)
            
    def size(self):
        c=0
        temp=self.head
        while temp!=None:
            temp=temp.next
            c=c+1
        print(c)
        
        
        
s=stack()
s.push(90)
s.push(8)
s.push(78)
s.display()
s.pop()
s.display()
s.peek()
s.isempty()
s.display()
s.size()
