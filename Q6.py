def push(stack,N):
    for a in N:
        if a%2 == 0:
            stack.append(a)
    print("The Stack of even numbers is --> ", stack)
def pop(stack):
    if stack == []:
        print("EMPTY STACK")
    else:
        print("The Popped contents of the stack are-")
        top = len(stack)-1
        for a in range (top, -1,-1):
            x = stack.pop()
            print(x,"",end=" ")
#__main__
N= [12,13,34,56,21,79,98,22,35,38]  #Sample Stack
stack=[]
while True:  
    c = int(input("\n....Menu....\nEnter 1 to create stack of even Numbers.\nEnter 2 to pop and display stack.\nEnter 3 to EXIT.\nEnter Your Choice:"))
    if c == 1:
        push(stack,N)
    elif c == 2:
        pop(stack)
    elif c == 3:
        break
    else:
        print("Invalid Input")
