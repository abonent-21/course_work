class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dequeue:
    def __init__(self, size=0):
        self.front = Node('Front')
        self.rear = Node('Back')
        self.size = size
    
    def is_empty(self):
        return self.front.prev is None
    
    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front.prev = new_node
            self.rear.next = new_node
        else:
            new_node.prev = self.front.prev
            self.front.prev.next = new_node
            self.front.prev = new_node
        self.size += 1

    
    def add_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front.prev = new_node
            self.rear.next = new_node
        else:
            new_node.next = self.rear.next
            self.rear.next.prev = new_node
            self.rear.next = new_node
        self.size += 1
    
    def remove_front(self):
        if self.is_empty():
            raise IndexError("No elememts to delete in queue")
        if self.size == 1:
            self.rear.next = None
            self.front.prev = None
        else:
            self.front.prev = self.front.prev.prev
            self.front.prev.next = None # очищаем стек от узлаx
        self.size -= 1
    
    def remove_back(self):
        if self.is_empty():
            raise IndexError("No elememts to delete in queue")
        if self.size == 1:
            self.rear.next = None
            self.front.prev = None
        else:
            self.rear.next = self.rear.next.next
            self.rear.next.prev = None
        self.size -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("No elememts to get in queue")
        return self.front.prev.data
    
    def get_back(self):
        if self.is_empty():
            raise IndexError("No elements to get in queue")
        return self.rear.next.data
    
    def pop_front(self):
        item = self.get_front()
        self.remove_front()
        return item

    def pop_back(self):
        item = self.get_back()
        self.remove_back()
        return item
    
    def get_size(self):
        return self.size

    
    
if __name__ == '__main__':
    queue = Dequeue()
    queue.add_front(1)
    queue.add_back(2)
    queue.add_front(3)
    queue.add_back(4)
    queue.add_back(4)
    queue.add_back(4)
    queue.add_back(4)
    queue.add_front(0)
    for i in range(8):
        queue.remove_back()

    def display(q):
            """Показать все элементы очереди"""
            if q.is_empty():
                print("Deque is empty!")
                return
            current = q.front.prev
            elements = []
            while current:
                elements.append(current.data)
                current = current.prev
            return elements

    print(display(queue))






