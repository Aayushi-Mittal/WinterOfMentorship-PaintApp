#Implicit Type Conversion
num=4
decimal_num=4.0
string="Hello World!"
print(type(num))
print(type(decimal_num))
print(type(string))

#Explicit Type Conversion
num=int(input("Enter a number: "))
decimal_num=float(input("Enter a floating number: "))
string= input("Enter a string: ")
print(type(num))
print(type(decimal_num))
print(type(string))

#Type Conversion of int to float
new_num1=float(num)
#Type Conversion of string to int
new_num2=int(string)