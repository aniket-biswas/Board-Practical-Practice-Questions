def isempty(stack):
    if stack == []:
        return True
    else:
        return False
def push(stack, age):
    stack.append(age)
def pop(stack):
    if isempty(stack):
        print("Stack Empty")
    else:
        x=stack.pop()
        return x
def traverse(stack):
    top = len(stack)-1
    for i in range(top,-1,-1):
        print(stack[i])
#__main__
Sport_Stack=[]
while True:
    c = int(input("....ENTER CHOICE....\nInsert Age --> 1\nPop Age --> 2\nDisplay --> 3\nExit --> 4\nEnter Your Choice: ")) 
    if c==1:
        age=int(input("Enter Age of Sportsman: "))
        push(Sport_Stack,age)
    elif c==2:
        x=pop(Sport_Stack)
        print("\nPopped element --> ",x)
    elif c==3:
        traverse(Sport_Stack)
    elif c == 4:
        break
    else:
        print("INVALID INPUT")
