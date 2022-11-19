class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SingleLinkedList:
   def __init__(self):
      self.headval = None

list1 = SingleLinkedList()
list1.headval = Node("January")
e2 = Node("February")
e3 = Node("March")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
