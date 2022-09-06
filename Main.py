
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Link:
  def __init__(self):
    self.head = None
    self.count = 0
  
  def push(self,data):
    new = Node(data)
    new.next = self.head
    self.head = new
    self.count += 1
  
  def search(self,target):
    n = self.head
    result = 0
    node_number = 0
    new = {}
    for i in range(self.count):
      if(n.data == target):
        new = {
            "postion:":i,
            "node value:":target
        }
    print()
    return new

        

  def pair(self):
    n = self.head
    while(n):
      print(n.data,end = "->")
      n = n.next
    print("\n")
    
  def delete_beg(self):
    temp = self.head
    self.head = self.head.next
    temp = None
  
  def delete_end(self):
    for i in range(self.count):
      if(i == self.count - 1):
        temp = self.head
        self.head.next = None
        temp = None


  def reverse(self):
    curr , prev , next = self.head , None,None
    while(curr != None):
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    self.head = prev

l1 = Link()
# while(1):
#   x = int(input())
#   if(x == 1):
#     val = int(input())
#     l1.push(val)
#   elif(x == 2):
#     l1.reverse()
#   elif(x == 3):
#     l1.pair()
#   elif(x == 4):
#     search = int(input())
#     print(l1.search(search))

for i in range(3):
  val = int(input())
  l1.push(val)

l1.pair()
l1.delete_beg()
l1.pair()
l1.delete_end()
l1.pair()
