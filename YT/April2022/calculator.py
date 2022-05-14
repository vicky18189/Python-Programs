from ast import operator

from pyparsing import opAssoc


first = input("Enter First Number: ")
operator = input("Enter Operator (+,-,*,/): ")
second = input("Enter Second Number: ")

if operator == "+":
    print(int(first) + int(second))
elif operator == "-":
    print(int(first) - int(second))
elif operator == "*":
    print(int(first) * int(second))
elif operator == "/":
    print(int(first) / int(second))
else:
    print("Invalid operator")