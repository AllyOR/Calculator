### CALCULATOR OPTIONS

print(" CALCULATOR ON. ")

# To add two numbers

def add(x, y):
    return (x + y)

# To substract two numbers

def substract(x, y):
    return (x - y)

# To multiply two numbers

def multiply(x, y):
    return (x * y)

# To divide two numbers

def divide(x, y):
    return (x / y)

# To give power to a number

def power(x, y):
    return pow(x, y)

print(" 1. Add")
print(" 2. Substract")
print(" 3. Multiply")
print(" 4. Divide")
print(" 5. Power\n")

### CALCULATOR

flag = True

while flag == True:
    
    choice = input("SELECT THE OPERATION: 1/ 2/ 3/ 4/ 5/ x to END \n")
    options = ["1","2","3","4","5"]
    
    if choice in options:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2), "\n")
        elif choice == "2":
            print(num1, "-", num2, "=", substract(num1, num2), "\n")
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2), "\n")
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2), "\n")
        elif choice == "5":
            print(num1, "^", num2, "=", power(num1, num2), "\n")
            
    elif choice == "x" or choice == "X":
        flag = False
        print(" CALCULATOR OFF. ")
        
    else:
        print(" Invalid Input ")
