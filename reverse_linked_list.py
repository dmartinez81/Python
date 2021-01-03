class Linkedlist:
    def __init__(self, data=None, next = None):
         self.head = data
         next = None

    def AddToList(self, NewData):
        NewNode = Node(NewData)
        if self.head is None:
            self.head = NewNode
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode

    def PrintElements(self):
        temp = self.head
        while temp:
            print(temp.data, end="   ")
            temp = temp.next
    
    def ReverseList(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        while prev:
            print(prev.data, end="   ")
            prev = prev.next

        self.head = prev

                           
class Node:
    def __init__(self, data=None, next=None):
        self.head = None
        self.data = data
        self.next = None

listA = Linkedlist()
listB = Linkedlist()

listA.AddToList(2)
listA.AddToList(3)
listA.AddToList(5)
listA.AddToList(7)
listA.AddToList(9)

listA.PrintElements()
print("\n\n")

listA.ReverseList()

print("Done")