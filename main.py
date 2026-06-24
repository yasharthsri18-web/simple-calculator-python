import math
print("\t______CALCULATOR______")

def get_two_numbers():
    a = int(input("\tEnter a number: "))
    b = int(input("\tEnter another number: "))
    return a,b 

def add(a,b):
    return a + b

def sub(a,b):
    return a-b
    
def multiply(a,b):
    return a*b

def div(a,b):
    if(b==0):
        raise ZeroDivisionError("\tHey our program doesn't support division of numbers by zero")
    c = format(a/b,'.2f')
    d = a%b
    return c,d

def sqrt(a):
    x = math.sqrt(a)
    return x

def cubrt(a):
    x = math.cbrt(a)
    return x

def sqr(a):
    return a*a

def cub(a):
    return a*a*a

def pwr(a,b):
    return a ** b

def mod(a):
    return abs(a)

while(True):
    print("\n\nChoose the operation you want to perform; ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE ROOT")
    print("\n\t6.CUBE ROOT")
    print("\n\t7.SQUARE")
    print("\n\t8.CUBE")
    print("\n\t9.POWER")
    print("\n\t10.ABSOLUTE VALUE")
    print("\n\t11.EXIT")

    choice = int(input("\tEnter your choice: "))
    
    if(choice == 1):
        a,b= get_two_numbers()
        c = add(a,b)
        print("\tThe sum of two numbers is: ",c)

    elif(choice == 2):
        a,b = get_two_numbers()
        c = sub(a,b)
        print("\tThe difference of two numbers is: ",c)

    elif(choice == 3):
        a,b = get_two_numbers()
        c = multiply(a,b)
        print("\tThe product of two numbers is: ",c)

    elif(choice == 4):
        a,b = get_two_numbers()
        c,d = div(a,b)
        print("\tThe quotient of the following division is: ",c)
        print("\tThe remainder of the following division is: ",d)

    elif(choice == 5):
        a = int(input("\tEnter a number : "))
        c = sqrt(a)
        print("\tThe square root of the given number is: ",c)

    elif(choice == 6):
        a = int(input("\tEnter a number : "))
        c = cubrt(a)
        print("\tThe cube root of the given number is: ",c)

    elif(choice == 7):
        a = int(input("\tEnter a number : "))
        c = sqr(a)
        print("\tThe square of the given number is: ",c)

    elif(choice == 8):
        a = int(input("\tEnter a number : "))
        c = cub(a)
        print("\tThe cube of the given number is: ",c)

    elif(choice == 9):
        a,b = get_two_numbers()
        c = pwr(a,b)
        print(f"\t{a} raised to the power {b} is: ",c)

    elif(choice == 10):
        a = int(input("\tEnter a number: "))
        c = mod(a)
        print("\tThe absolute value of the given number is: ",c)

    else:
        print("\n\tEXIT")
        break

print("\tOPERATION COMPLETED")



    


