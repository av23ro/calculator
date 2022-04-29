print("<----CALCULATOR---->")
while True:
    print("")
    print("OPTIONS:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    print("")
    ch=int(input("Enter your choice:"))
    if ch==1:
        val1=int(input("enter number 1:"))
        val2=int(input("enter number 2:"))
        print("<<--Addition-->>")
        val3=val1+val2
        print("result=",val3)
    elif ch==2:
        val1=int(input("enter number 1:"))
        val2=int(input("enter number 2:"))
        print("<<--Subtraction-->>")
        val3=val1-val2
        print("Result=",val3)
    elif ch==3:
        val1=int(input("enter number 1:"))
        val2=int(input("enter number 2:"))
        print("<<--Multiplication-->>")
        val3=val1*val2
        print("Result=",val3)
    elif ch==4:
        val1=int(input("enter number 1:"))
        val2=int(input("enter number 2:"))
        print("<<--Division-->>")
        val3=val1/val2
        print("Result=",val3)
    elif ch==5:
        print("THANK YOU")
        break
    else:
        print("Invalid Choice!!!")

    
    
