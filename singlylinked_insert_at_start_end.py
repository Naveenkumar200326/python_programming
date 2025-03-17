class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class singlylinklist:
    def __init__(self):
      self.head=None
      
    def insertatbegin(self,data):
      newnode=Node(data)
      newnode.next=self.head
      self.head=newnode
      
    def insertatend(self,data):
      newnode=Node(data)
      if(self.head==None):
        self.head=newnode
        return
      temp=self.head
      while temp.next:
        temp=temp.next
      temp.next=newnode
      
    def display(self):
      temp=self.head
      while temp:
        print(temp.data,end=" ")
        temp=temp.next
s=singlylinklist()
n=int(input())
for i in range(0,n):
  x=int(input())
  s.insertatend(x)
y=int(input())
s.insertatbegin(y)
s.display()


