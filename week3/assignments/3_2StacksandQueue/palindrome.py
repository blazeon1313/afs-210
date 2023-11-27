class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next 

class Stack:
    def __init__(self):
        self.stack = None

    def push(self, data):
        node = Node(data, self.stack)
        self.stack = node

    def pop(self):
        data = self.stack.data
        self.stack = self.stack.next
        return data
    
    def isEmpty(self):
        return self.stack == None
    def __str__(self):
        if self.stack is None:
            return None
        node = self.stack
        result = "["
        while node is not None:
            result += str(node.data) + " "
            node = node.next
        return result[:-1] + "]"

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        data = self.head.data
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.head = self.head.next
        return data
    
    def isEmpty(self):
        return self.head is None

    def __str__(self):
        if self.head is None:
            return None
        node = self.head
        result = "["
        while node is not None:
            result += str(node.data) + " "
            node = node.next
        return result[:-1] + "]"
    
def isPalindrome(z):

    stack = Stack()
    queue = Queue()
        
    for x in z:
        stack.push(x)
        queue.enqueue(x)
    while not stack.isEmpty():
        if stack.pop() != queue.dequeue():
            return False
    return True

print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))