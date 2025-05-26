class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertatFront(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end= ' ')

            temp=temp.next
        print()

    def insertAtEnd(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return None
        last=self.head

        while last.next:
            last=last.next
        last.next=new_node

if __name__ ==  '__main__':
    llist=LinkedList()

    llist.insertatFront("Fox")
    llist.insertatFront("Brown")
    llist.insertatFront("Quick")
    llist.insertatFront("The")
    llist.insertAtEnd("Jumps")
    llist.insertAtEnd("Over")
    llist.insertAtEnd("The")
    llist.insertAtEnd("Fence")

    llist.printLinkedList()




