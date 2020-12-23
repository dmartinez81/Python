class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.data = None
        self.next = None

    def AddToList(self, NewData):
        NewNode = Node(NewData)
        if self.head is None:
            self.head = NewNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = NewNode 

def MergeLists(headA, ListB):
    DummyNode = Node(0)
    tail = DummyNode

    while True:
        if not ListA:
            tail.next = headB
            break

        if not ListB:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    return DummyNode.next

    
ListA = LinkedList()
ListB = LinkedList()
ListC = LinkedList()

ListA.AddToList(2)
ListA.AddToList(3)
ListA.AddToList(5)

ListB.AddToList(4)
ListB.AddToList(7)
ListB.AddToList(10)

ListC.head = MergeLists(ListA.head, ListB.head)

print("Done")




