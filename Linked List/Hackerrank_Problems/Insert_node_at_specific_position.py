'''
PROBLEM: INSERT A NODE AT A SPECIFIC POSITION AT A LINKED LIST
'''

import math
import os
import random
import re
import sys

# The node class
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

# The Singly Linked List class.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Method to extend the Linked list
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    # Method to print a given linked list.
    def print_singly_LL(self, sep, list):
        while node:
            print(str(node.data))

            node = node.next

            if node:
                print(sep)

##########################################################
''' Function to add a new data point at a given position'''
###########################################################

def insertNodeAtPosition(head,data, position):
    node_next = None
    for i in range(position-1):
        if node_next is None:
            node_next = head.next
            node_next_to_next = node_next.next

        else:
            node_next = node_next.next
            node_next_to_next = node_next.next

    node_next.next = SinglyLinkedListNode(data)
    node_next.next.next = node_next_to_next

    return(head)


##########################################################
             ''' Calling the Function '''
##########################################################

# input linked list size
llist_count = int(input("Enter the size of Input LinkedList\n"))
llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input("Enter the number"))
    llist.insert_node(llist_item)

data = int(input("Enter the data to be Inserted \n"))
position = int(input("Enter the position at which you want to insert \n"))

llist_head = insertNodeAtPosition(llist.head, data, position)

print_singly_LL(llist_head, '', fptr)
