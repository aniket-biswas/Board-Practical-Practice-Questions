def isempty(stack):
    if stack == []:
        return True
    else:
        return False
def push(stack, vow):
    stack.append(vow)
def pop(stack):
    if isempty(stack):
        print("Stack Empty")
    else:
        x=stack.pop()
        print("The popped element is:",x)
def traverse(stack):
    top = len(stack)-1
    for i in range(top,-1,-1):
        print(stack[i])
#__main__
StackVow=[]
Vowel=["a","e","i","o","u","A","E","I","O","U"]
while True:
    ch = int(input("....ENTER CHOICE....\nPush vowel --> 1\nPop --> 2\nDisplay --> 3\nEnter Your Choice:"))
    if ch==1:
        vow = input("Enter Vowel: ")
        if vow in Vowel:
            push(StackVow,vow)
        else:
            print("Error: Inserted Value is Not Vowel")
    elif ch==2:
        pop(StackVow)
    elif ch==3:
        traverse(StackVow)
    elif ch==4:
        break
    else:
        print("Invalid Input")
        continue