class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.length=0

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.length=1
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
            self.length+=1

    def print_list(self):
        if self.head==None:
            print("Empty List")
        else:
            current_node=self.head
            while current_node!=None:
                print(current_node.data,end=" ")
                current_node=current_node.next
        print()

    def prepend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.length+=1
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.length+=1

    def insert(self,data,pos):
        new_node=Node(data)
        if pos>0 and self.head==None:
            print("No list found")
        elif pos==0:
            self.prepend(data)
        elif pos>=self.length:
            if pos>self.length:
                print("Position Exceeds Length. Inserting at the end of the list")
            new_node.prev=self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_node=self.head
            for i in range(pos-1):
                current_node=current_node.next
            new_node.prev=current_node
            new_node.next=current_node.next
            current_node.next=new_node
            self.length+=1

    def remove(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
        current_node = self.head
        while current_node!= None and current_node.next.data != data:
            current_node = current_node.next
        if current_node!=None:
            current_node.next = current_node.next.next
            if current_node.next != None: #If the node deleted is not the last node(i.e., the node next to the next to the current node is !- None),
                current_node.next.previous = current_node #Then we set the previous of the node next to the deleted node equal to the current node, so a two-way link is established
            else:
                self.tail = current_node #If the deleted node is the last node then we update the tail to be the current node
            self.length -= 1

my_linked_list = DoublyLinkedList()  
my_linked_list.print_list() #Empty List

my_linked_list.append(5)            
my_linked_list.append(2)
my_linked_list.append(9)
my_linked_list.print_list() #5 2 9

my_linked_list.prepend(4)
my_linked_list.print_list() #4 5 2 9

my_linked_list.insert(7,2)
my_linked_list.print_list() #4 5 7 2 9

my_linked_list.insert(0,0)  
my_linked_list.insert(6,4)
my_linked_list.insert(3,9)  #Position Exceeds Length. Inserting at the end of the list
my_linked_list.print_list() #0 4 5 7 6 2 9 3 

my_linked_list.remove(3)
my_linked_list.print_list() #0 4 5 7 2 9 0

print(my_linked_list.length)