# try:
#     n1=int(input("Enter a number:"))
#     n2=int(input("Enter a number:"))
#     r=n1/n2
#
# except ValueError:
#     print("valueerror")
# except ZeroDivisionError:
#     print("Zero division error")
# else:
#     print("result",r)
# finally:
#     print("done")

# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

# import math
# while(True):
#     try:
#         num=int(input("Enter a number:"))
#         fact=math.factorial(num)
#     except ValueError:
#         print("value error.Please enter correct number")
#         continue
#     else:
#         print("Factorial:",fact)
#         break
#     finally:
#         print("Done")

# #using function
# import math
# def fact():
#     try:
#         num=int(input("Enter a number:"))
#         f=math.factorial(num)
#         print("Factorial:",f)
#     except ValueError:
#         print("value error.Please enter correct number")
#         fact()
#     else:
#         pass
# fact()

# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         result = a + b
#     elif choice == 2:
#         result = a - b
#     elif choice == 3:
#         result = a * b
#     elif choice == 4:
#         result = a / b
#     else:
#         exit()
#
# except ValueError:
#     print("Invalid input. Enter numbers only.")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# else:
#     if result is not None:
#         print("Result:", result)
#
# finally:
#     print("Calculator program completed.")
    

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     filename = input("Enter filename: ")
#     f = open(filename, "r")
#     s = f.read()
#
# except FileNotFoundError:
#     print("File does not exist")
#
# else:
#     print(s)
#     f.close()




#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

# d = {"name": "arun", "age": 23, "place": "ekm"}
#
# try:
#     key = input("Enter key: ")
#     value = d[key]
#
# except KeyError:
#     print("Key does not exist")
#
# else:
#     print("Value:", value)
#
# finally:
#     print("Dictionary operation completed")

#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
try:
    n=int(input("Enter a number:"))
    if n<=0:
        raise ValueError ("Number Must Be Positive")
except ValueError as e:
    print(e)
#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")