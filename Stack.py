class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def pop(self):
        del self.items[-1]
    def peek(self):
        print(self.items)
    def size(self):
        return len(self.items)
def main():
    myStack=Stack()
    myStack.push("óla")
    myStack.push("eu")
    myStack.push("sou")
    myStack.peek()
    myStack.pop()
    myStack.peek()
    myStack.pop()
    myStack.peek()
    print(myStack.size())
    myStack.push("Guilherme")
    print(myStack.size())