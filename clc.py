import math

def menu():
    print("-----------Menu Bar------------")
    print("----------1.Addition-----------")
    print("----------2.Subtraction--------")
    print("----------3.Raise to power-----")
    print("----------4.Divison------------")
    print("----------5.Multiplication-----")
    print("----------6.Floor Devision-----")
    print("----------7.factorial----------")
    n=int(input("Enetr the value of key:- "))
    if(n==1):
       add()
    elif(n==2):
         sub()
    elif (n == 3):
        powe()
    elif (n == 4):
        div()
    elif (n == 5):
        mul()
    elif (n == 6):
        flo()
    elif (n == 7):
        x = int(input("Enter the value of x:-"))
        fact(x)

def add():
    x = int(input("Enter the value of x:-"))
    y = int(input("Enter the value of y:-"))
    print(" Addition :-",(x+y))
    n=int(input("you want to Program continue,Enter the value of Zero:-"))
    if(n==0):
        menu()

def sub(x, y):
    x = int(input("Enter the value of x:-"))
    y = int(input("Enter the value of y:-"))
    print(" substraction :-" , (x - y))
    n = int(input("you want to Program continue,Enter the value of Zero:-"))
    if (n == 0):
        menu()

def powe(x,y):
    x = int(input("Enter the value of x:-"))
    y = int(input("Enter the value of y:-"))
    print("Power of raised:_",(x**y))
    n = int(input("you want to Program continue,Enter the value of Zero:-"))
    if (n == 0):
        menu()
1
def mul(x, y):
    x = int(input("Enter the value of x:-"))
    y = int(input("Enter the value of y:-"))
    print(" Multiplication :-%d" % (x * y))
    n = int(input("you want to Program continue,Enter the value of Zero:-"))
    if (n == 0):
        menu()

def div(x, y):
    x = int(input("Enter the value of x:-"))
    y = int(input("Enter the value of y:-"))
    print(" divison :-%f" % (x / y))
    n = int(input("you want to Program continue,Enter the value of Zero:-"))
    if (n == 0):
        menu()

def flo(x, y):
    x = int(input("Enter the value of x:-"))
    y = int(input("Enter the value of y:-"))
    print("  Floor divison :-%f" % (x // y))
    n = int(input("you want to Program continue,Enter the value of Zero:-"))
    if (n == 0):
        menu()

def fact(x):
    print("factorial:-",math.factorial(x))
    n = int(input("you want to Program continue,Enter the value of Zero:-"))
    if (n == 0):
        menu()

menu()

