class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node

    def removeNode(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return self
        runner = self.head
        while runner.next != None:
            if runner.next.value == value:
                print(id(runner.next),runner.next.value)
                runner.next = runner.next.next
                return self
            runner = runner.next

    def displayAll(self, msg):
        runner = self.head
        print("="*10 + " START PROGRAM " + "="*10)
        print("head point is "+ str(id(runner)))
        print("Printing value in the list: "+ msg)
        while runner.next != None:
            print("true", id(runner), runner.value, id(runner.next))
            runner = runner.next
        print("false", id(runner), runner.value, id(runner.next))

list = Slist(5)
list.addNode(4)
list.addNode(3)
list.addNode(2)
list.displayAll("first try")

list.removeNode(2)
list.displayAll("second try")
