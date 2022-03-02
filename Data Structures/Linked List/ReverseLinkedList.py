# from Implementation import LinkedList,Node

# my_linked_list = LinkedList()
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.print_list() #2 3 4

# def reverse(linked_list):
#     if linked_list.length <=1:
#         return linked_list
#     else:
#         first=linked_list.head
#         second=first.next
#         while second != None:
#             temp=second.next
#             second.next=first
#             first=second
#             second=temp
#         linked_list.head.next=None
#         linked_list.head=first
#         return linked_list

# reversed_linked_list = reverse(my_linked_list)
# reversed_linked_list.print_list()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
 
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
llist.printList()
print()
llist.reverse()
llist.printList()