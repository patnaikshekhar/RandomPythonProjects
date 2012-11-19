class ListNode:
    item = 0
    next = None
    def __init__(self, item, next):
        self.item = item
        self.next = next

    def insertAfter(self, item):
        self.next = ListNode(item, self.next)

    def printList(self):
        print self.item
        if not self.next:
            return
        else:
            self.next.printList()
        return

    def nth(self, position):
        if position == 1:
            return self
        elif position < 1 or not self.next:
            return None
        else:
            return self.next.nth(position - 1)

class LinkedList
    head = None
    size = 0

    def __init__(self):
        head = None
        size = 0

    def insertFront(self, item):
        head = ListNode(item)
        size = size + 1
        
a = ListNode(1, None)
a.insertAfter(10)
a.next.insertAfter(11)

print a.nth(3).item
