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
       while temp.next:
           temp = temp.next
       temp.next = Node(data,None)

    def insert_Values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_len(self):
        c = 0
        t = self.head
        while t:
            c += 1
            t = t.next
        return c
    def remove(self,index):
        if index < 0 or index >= self.get_len():
            raise Exception("Invalid Index")
        if index == 0:
           self.head = self.head.next
        t = self.head
        c = 0
        while t:
            if c == index - 1:
                t.next = t.next.next
                break
            c += 1
            t = t.next

    def insert_At(self,index,data):
        if index < 0 or index >= self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        t = self.head
        c = 0
        while t:
            if c == index - 1:
                n = Node(data,t.next)
                t.next = n
                break
            c += 1
            t = t.next

if __name__ == '__main__':
     l = LinkedList()
     l.insert_Values(['mango','banana','papaya'])
     l.print()
     print("length ", l.get_len())
     # l.remove(1)
     # l.print()
     l.insert_At(0,"banana")
     l.print()
     print("length ",l.get_len())


