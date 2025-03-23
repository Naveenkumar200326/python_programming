class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly:
    def __init__(self):
        self.head=None
        
    def insertatbegin(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
            return
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode
    def insertatend(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
        
    def deleteatbegin(self):
        self.head=self.head.next
        
    def deleteatend(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
    
    def insertatposition(self,data,pos):
        
        newnode=Node(data)
        if(pos==1 or self.head==None):
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
            return
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        if(temp.next!=None):
            newnode.next=temp.next
            temp.next.prev=newnode
            newnode.prev=temp
            temp.next=newnode
            return
        temp.next=newnode
        newnode.prev=temp
    
    def deleteatposition(self,pos):
        if(pos==1):
            self.head=self.head.next
            return
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        if(temp.next.next==None):
            temp.next=None
            return
        temp.next.next.prev=temp
        temp.next=temp.next.next
        
s=doubly()
s.insertatbegin(10)
s.insertatbegin(20)
s.insertatbegin(30)
s.insertatend(40)
s.insertatend(50)
s.insertatbegin(60)
s.deleteatbegin()

s.display()
s.deleteatend()
s.display()
s.insertatposition(99,3)
s.display()
s.insertatposition(100,6)
s.display()
s.deleteatposition(6)
s.display()
