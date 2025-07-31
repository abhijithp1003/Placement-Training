class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    
    def display(self):
        if not self.head:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            print("The linked list is:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def delete(self, a):
        if not self.head:
            print("Linked List is empty")
            return
        elif(a == 1):
            temp = self.head
            self.head = temp.next
            temp = None
        else:
            prev = None
            temp = self.head
            for i in range(1, a):
                prev = temp
                temp = temp.next
                if temp is None:
                    print("Position out of range")
                    return
            
            prev.next = temp.next

l = LinkedList()
l.add(1)
l.add(18)
l.add(17)
l.add(19)
l.delete(6)
l.display()