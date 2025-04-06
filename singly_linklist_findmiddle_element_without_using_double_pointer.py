
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class singly:
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
  
  def findelement(self,pos):
    count=0
    temp=self.head
    while temp:
      count+=1
      temp=temp.next
    
    if pos>count or pos<=0:
      print("Invalid position")
      return
    
    index=count-pos
    temp=self.head
    for i in range(index):
      temp=temp.next
    print(temp.data)
    
  def middleelement(self):
    count=0
    temp=self.head
    while temp:
      count+=1
      temp=temp.next
      
    index=count//2
    temp=self.head
    for i in range(index):
      temp=temp.next
    print(temp.data)
    
    
    
s=singly()
x=0
while x!=-1:
  x=int(input())
  if x!=-1:
    s.insertatend(x)
pos=int(input())
s.middleelement()
s.findelement(pos)
