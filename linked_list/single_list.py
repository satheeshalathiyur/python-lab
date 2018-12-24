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

llist = LinkedList()
first = Node(1) #first node
llist.head = first
second = Node(2) #second node
first.next = second
third = Node(3)
second.next = third
llist.traverse()