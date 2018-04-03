# Day 15 coding challenge - Linked List

# Complete the insert function in your editor so that it creates a new Node (pass data as
# the Node constructor argument) and inserts it at the tail of the linked list referenced by
# the head parameter. Once the new node is added, return the reference to the head
# node.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.n˜ext

    def insert(self, head, data):
        mylist= Solution()
        node = Node(data)
        if head is None:
            head = node
        else:
            current = head
            while(current.next is not None):
                current = current.next
            current.next = node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);