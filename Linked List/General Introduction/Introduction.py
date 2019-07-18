''' Introduction to the LinkedList '''

'''
A linked list is a sequence of elements, which are connected together via links.
Each data element contains a connection to another data element in form of a
pointer.

Python does not have linked lists in its standard library. We implement the concept
of linked lists using the concept of nodes. We can create an object 'node' which
has following attributes, it stores a data element, and has a pointer to the next
node.

Let us first start with implementing the singly linked lists. IN this type of
data structures there is only one link between any two nodes or data containing
elements. We create such a list and create additional methods to insert, update
and remove elements from the list.

'''

'''
CREATION OF THE LINKED LIST and Adding a method to traverse it.
'''
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def printLL(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

# Defining an instance of class LinkedList.
list1 = LinkedList()

# Defining its head node and getting it a value.
list1.headval = Node(1)

# Let us add some more nodes.
list1.headval.nextval = Node(2)

# Calling the print function.
list1.printLL()
