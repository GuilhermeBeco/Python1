def useStack():
    stack=[]
    opt=-1
    while opt!=4:
        print("1. Puch to stack")
        print()
        print("2. Pop from stack")
        print()
        print("3. Print stack")
        print()
        print("4. Exit")
        opt=int(input("Enter your opt: "))
        if opt==1:
            nextItem=input("What do you want to add:" )
            stack.apend(nextItem)
        if opt==2:
            print ("The last one in was {0}".format(stack[-1]))
            print ("This is the one i am going to delet4")
            del stack[-1]
        if opt==3:
            for counter in range(len(stack)-1,-1,-1):
                print(stack[counter])