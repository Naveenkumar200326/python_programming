
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
    
  def display(self):
    temp=self.head
    while temp:
      print(temp.data,end=" ")
      temp=temp.next
      
  def insertatmid(self,data,pos):
    temp=self.head
    newnode=Node(data)
    if(pos==1):
      newnode.next=self.head
      self.head=newnode
      return
    for i in range(pos-2):
      temp=temp.next
    if(temp.next!=None):
      newnode.next=temp.next
      temp.next=newnode
      return
    temp.next=newnode
s=singlylinklist()
n=int(input())
for i in range(0,n):
  x=int(input())
  s.insertatend(x)
pos=int(input())
data=int(input())
s.insertatmid(data,pos)
s.display()
