import math
import sys


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x , y):
    return x * y

def divition(x , y):
    if y == 0:
        print('Error! Divition by zero is not allowed..')
        
        while True:
            try:
                num1 = float(input("Enter the firts number: "))
                num2  = float(input("Enter the second number: "))
                if num1.is_integer() and num2.is_integer(): 
                    return divition(num1, num2)
            except ValueError:
                print("Invalid input, enter a number")
    else:
        return x / y
    
    
def power(x ,  y):
    return x ** y 

def square(x):
    if x < 0:
        print('Error! Cannot calculate the square of  a negative number.')
        print("Enter a positive number")
        while True:
                try:
                    num = float(input("Enter a number: ")) 
                    if num.is_integer():
                        return  square(num)                          
                except ValueError:
                    print("Invalid input, Enter a number")    
    else:
       return math.sqrt(x)
        
        
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.sin(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))


def simple_calculator():
    
    while True:
        print("Select an option\n")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Mutliply")
        print("4 - Divition")
        print("5 - Power (Exponential)")
        print("6 - Square")
        print("7 - Sine")
        print("8 - Cosine")
        print("9 - Tangent")
        print("10 - Quit")
        
        choice = input("\nEnter a choice (1/2/3/4/5/6/7/8/9/10): ")
        
        if choice in ("1", "2", "3" , "4", "5"):
            while True:
                try:
                    num1 = float(input("Enter the firts number: "))
                    num2  = float(input("Enter the second number: "))
                    
                    if num1.is_integer() and num2.is_integer():
                        
                        if choice == "1":
                            print("Results = ", add(num1, num2))
                            break
                        elif choice == "2":
                            print("Results = ", subtract(num1, num2))
                            break
                        elif choice == "3":
                            print("Results = ", multiply(num1,num2))
                            break
                        elif choice == "4":
                            print("Results = ", divition(num1, num2))
                            break
                        elif choice == "5":
                            print("Results = ",power(num1, num2) )  
                            break
                except ValueError:
                    print("Invalid input,Enter a number") 
                    
        elif choice == "6":
            while True:
                try:
                    num = float(input("Enter a number: "))   
                    if num.is_integer():
                        print("Results = ", square(num))
                        break    
                except ValueError:
                    print("Invalid input, Enter a number")      
                    
        elif choice in ("7" , "8" , "9"):
            while True:
                try:
                    angle = float(input("Enter an angle in degrees: "))
                    if angle.is_integer():
                        if choice == '7':
                            print('Results = ', sin(angle)) 
                            break
                        elif choice == '8':
                            print("Results = ", cos(angle))
                            break
                        elif choice == '9':
                            print('Results = ', tan(angle)) 
                            break         
                except ValueError:
                    print("Invalid input , enter an angle in degrees.")    
        
        elif choice == "10":
            print("Thank you for using this Calculator")
            print("Exiting...")
            print("Goodbye.")
            sys.exit()    
            
        else:
            print("Invalid input")                            
                            
                            
        
    
print("\nWelcome to the Python Calculator\n")
simple_calculator()    
                   
    