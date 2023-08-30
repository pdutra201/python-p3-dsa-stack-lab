class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
       
    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None
        

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

        

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        distance = 0
        for item in self.items[::-1]:  # Iterate from the top of the stack downwards
            if item == target:
                return distance
            distance += 1
        return -1
