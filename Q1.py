def isEmpty(stack):
    if stack==[]:
        return True
    else:
        return False
def Insert(stack):
    while True:
        roll = int(input("\nEnter Roll No: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        student = [roll, name, marks]
        stack.append(student)
        choice=int(input("\n....Enter choice:....\nInsert Again --> 1\nExit --> 2\n"))
        if choice == 1:
            continue
        elif choice == 2:
            break
        else:
            print("Invalid Input")
            break
        top=len(stack) - 1
def display(stack,rank):
    if isEmpty(stack):
        print("Stack Empty")
    else:
        top = len(stack) - 1
        m=[]
        for a in range(top,-1,-1):
            s=stack[a]
            p=s[2]
            m.append(p)
        m.sort()
        per= (top - rank)
        for a in range(top,-1,-1):
            s=stack[a]
            if s[2] == m[per]:
                print(s)
def pop(stack,percent):
    if isEmpty(stack):
        print("Empty Stack")
    else:
        top = len(stack) - 1
        m=[]
        for a in range(top,-1,-1):
            s=stack[a]
            if s[2] < percent:
                x=stack.pop(a)
                print("Popped item--> ",x)
        print("\nThe Required Stack is:\n ",stack)
        
                
#__main__
stack = []
top= None
while True:
    c=int(input("....Operation Menu....\nInsert Record --> 1\nView Student Details --> 2\nRemove record by Minimum Percentage -->3\nExit-->4\nEnter Your Choice:"))
    if c == 1:
        Insert(stack)
    elif c == 2:
        rank= int(input("Enter Rank Of student to view:"))
        display(stack,rank)
    elif c == 3:
        percent= int(input("Enter Minimum Percent: "))
        pop(stack,percent)
    elif c == 4:
        break
    else:
        print("Invalid Input")