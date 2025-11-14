def calc():
    c=input("enter your choice  [+,-,/,*]")   
    a=float(input("enter first number"))
    b=float(input("enter second number"))
    if c == "+":
        print("The Addition Of Given Two Numbers :",a+b)
    elif c=="-":
        if a>b:
            print("Subtraction Of Given Two Number",a-b)
        else:
             print("Subtraction Of Given Two Number",b-a)
    elif c=="*":
        print("The Multiplication Of Two Numbers :",a*b)
    elif c=="/":
        print("The Division Of GIven Two numbers :",a/b)
    else:
        print("choice is in correct")

calc()
