from waitlist import *
class Node:
    def __init__(self, first_name, last_name):
        temp = Student(first_name,last_name)
        self.data = temp
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def __str__(self):
        studs = "Waitlist Status: "
        node = self.head
        if node is not None:
            for n in self:
                stud = n.data
                studs += stud.first_name + " " + stud.last_name
                if n.next is not None:
                    studs += " -- "
            return f"{studs} \nSize is {self.size}"
        return f"{studs} Empty"
    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = self.head.next
        self.size -= 1
        print(current_head.data, end=" ")
        print("has been moved off the waitlist")
        return current_head
    def add(self,first_name, last_name):
        new_node = Node(first_name, last_name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if not current.next:
                    break
                current = current.next
            current.next = new_node
        self.size += 1
    def is_empty(self):
        return not self.head
