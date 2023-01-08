import os 
def calculate(firstnum,secondnum,opperator):
    ans = 0
    if opperator == "+":
        ans = firstnum + secondnum
    elif opperator == "-":
        ans = firstnum - secondnum
    elif opperator == "*":
        ans = firstnum * secondnum
    else:
        ans = firstnum / secondnum
    print("%s %s %s = %s" % (firstnum , opperator ,  secondnum , ans))
    next = input("Type 'y' to continue calculating with %s , or type 'n' to start a new calculation : " % ans)
    if next == "y":
        opperator = input("Pick an Operation : ")
        secondnum = int(input("Whats the next number ? : "))
        calculate(ans,secondnum,opperator)
    else:
        os.system('cls')
        first = int(input("Whats the first number ? : "))
        print("+ \n- \n* \n/")
        opperator = input("Pick an Operation : ")
        secondnum = int(input("Whats the next number ? : "))
        calculate(firstnum,secondnum,opperator)
first = int(input("Whats the first number ? : "))
print("+ \n- \n* \n/")
operation = input("Pick an Operation : ")
second = int(input("Whats the next number ? : "))
calculate(first,second,operation)