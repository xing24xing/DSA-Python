class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List Is Empty")
            return
        temp = self.head
        llstr = " "
        while temp:
            llstr += str(temp.data) + " -> "
            temp = temp.next
        print(llstr+"Null")

    def insert_at_end(self,data):
       if self.head is None:
           self.head = Node(data,None)
           return
       temp = self.head
       while temp:
           temp = temp.next
       temp.next = Node(data,None)
    def insert_Values(self,data_list):
        self.head = None


if __name__ == '__main__':
     l = LinkedList()
     # l.insert_at_bregining(23)
     # l.insert_at_bregining(45)
     l.insert_at_end(45)
     l.insert_at_begining(89)
     # l.insert_at_end(3455)
     l.insert_at_begining(56)
     l.insert_at_begining(89)
     l.print()


