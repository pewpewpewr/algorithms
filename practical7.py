class QueueNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Queue:

    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0     
    def enqueue(self, element):
        node = QueueNode(element)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        if self.is_empty():
            self.tail = None

        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def count(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def to_string(self):
        if self.is_empty():
            return ""

        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

        return ", ".join(values)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.to_string())  
print(queue.count())      
print(queue.peek())      
print(queue.dequeue())    
print(queue.to_string())  
queue.clear()
print(queue.to_string())  