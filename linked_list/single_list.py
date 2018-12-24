'''
Node and LinkedList
Node: create node with data and next with empty
'''

# Creating linked list  & traverse a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    ''' Initialize head'''
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def insert_at_front(self,new):
        new.next = self.head
        self.head = new

    def insert_at_end(self,new):
        temp = self.head
        while temp and temp.next!=None:
            temp = temp.next
        temp.next = new

llist = LinkedList()
first = Node(1) #first node
llist.head = first
second = Node(2) #second node
first.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
sixth = Node(6)
fifth.next = sixth
print ('***********Traverse*******************')
llist.traverse()
print ('***************Insert at the front *************')
fourth = Node(0)
llist.insert_at_front(fourth)
print ('traverse after insert at front')
llist.traverse()
print ('***************Insert at the end *************')
seven = Node(7)
llist.insert_at_end(seven)
print ('traverse after insert at end')
llist.traverse()