#TASK ONE: NUMBERS AND VARIABLES
''' 1.Create three variables in a single line and assign different values to them and make sure their 
 data types are different. Like one is int, another one is float and the last one is a string.'''
integer,string,floatvar = 1,"Geoff",4.12
print(integer,string,floatvar)#output: 1 Geoff 4.12

'''2.Create a variable of value type complex and swap it with another variable whose value is an 
 integer.'''
complex_number,integer = 2+3j,3
print(complex_number,integer)#output: (2+3j) 3
#Swapping
complex_number,integer = integer,complex_number
print(complex_number,integer)#output: (2+3j) 3

'''3.Swap two numbers using the third variable as result name and do the same task without using 
 any third variable.'''
# Swapping using a third variable
x,y = 1,2
temp = x
x = y
y = temp
print(x,y)#output: 2 1
# Swapping without a third variable
x,y = y,x

'''4.Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.'''
#for Python 2.x and 3.x input() function can be used to give user input
name = input("Enter your name:")
print('My name is:', name)

'''5.Write a program to complete the task given below:
 Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
 Use z for adding 30 into it and print the final result by using variable result.'''
first_number = input("Enter the first number to add: ")
print(first_number)
second_number = input("Enter the second number to add: ")
print(second_number)
z = first_number+second_number
final_result = z + 30
print(final_result)

''' 6.Write a program to check the data type of the entered values. 
 HINT: Printed output should say -  The input value data type is: int/float/string/etc'''
float_variable = 4.134
print("Data type of float_variable is:",type(float_variable))#Data type of float_variable is:<class 'float'>

''' 7.Create Variable using CamelCase, LadderCase and UPPERCASE. 
# (Refer:   https://capitalizemytitle.com/camel-case/) - Variable Conventions to write'''
camelcase = "MyNameIsGeoff"
laddercase = "my_name_is_geoff"
uppercase = "GEOFF"

'''8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned 
to ‘a’ again. Will it change the value. If Yes then Why?'''
#Yes, will change the data type because Python is a dynamically typed programming language.
# Example
integer = 1
print(type(integer))#<class 'int'>
integer = 4.12
print(type(integer))#<class 'float'>
