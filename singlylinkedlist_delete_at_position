#Start your Coding Race
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class singlylinklist:
  def __init__(self):
    self.head=None
    
  def insertatend(self,data):
    newnode=Node(data)
    if(self.head==None):
      self.head=newnode
      return
    temp=self.head
    while temp.next!=None:
      temp=temp.next
    temp.next=newnode
    
  def deleteinpos(self,pos):
    if(pos==1):
      self.head=self.head.next
      return
    temp=self.head
    for i in range(pos-2):
      temp=temp.next
    temp.next=temp.next.next
    
    
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data,end=" ")
      temp=temp.next;
      
      
s=singlylinklist()
n=int(input())
for i in range(0,n):
  x=int(input())
  s.insertatend(x)
y=int(input())
s.deleteinpos(y)
s.display()
      
    
