import Stack
def useStack(stack):

    opt=-1
    while opt!=4:
        print("1. Push to stack")
        print()
        print("2. Pop from stack")
        print()
        print("3. Print stack")
        print()
        print("4. Exit")
        opt=int(input("Enter your opt: "))
        if opt==1:
            nextItem=input("What do you want to add: ")
            stack.push(nextItem)
        if opt==2:
            print ("This is the one i am going to delete: {0}".format(stack.items[-1]))
            stack.pop()
        if opt==3:
           stack.peek()