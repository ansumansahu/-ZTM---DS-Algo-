class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
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
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            current_node=self.head
            for i in range(pos-1):
                current_node=current_node.next
            new_node.next=current_node.next
            current_node.next=new_node
            self.length+=1

    def remove(self,data):
        if self.head==None:
            print("Empty List. Nothing to remove")
        current_node=self.head
        while current_node.next.data!=data:
            current_node=current_node.next
        if current_node.next!=None:
            current_node.next=current_node.next.next
        self.length -= 1

if __name__=='__main__':
    llist=LinkedList()
    llist.insert(2,3)   #No List Found
    llist.insert(2,0)   
    llist.print_list()  #2
    llist.insert(3,5)   #Position Exceeds Length. Inserting at the end of the list
    llist.print_list()  #2 3
    llist.append(8) 
    llist.append(10)
    llist.print_list()  #2 3 8 10
    llist.prepend(1)
    llist.print_list()  #1 2 3 8 10
    llist.insert(4,3)
    llist.print_list()  #1 2 3 4 8 10
    llist.insert(0,0)
    llist.print_list()  #0 1 2 3 4 8 10
    llist.remove(3)
    llist.print_list()  #0 1 2 4 8 10
    print(llist.length) #6