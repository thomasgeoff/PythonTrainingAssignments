# WEEKEND ACTIVITY ON FUNCTIONS
#Note: Assuming all inputs to functions are valid

# 1.Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”
#ANSWER:
def reverse_string(st):
  print(st[::-1])#dcba4321
reverse_string("1234abcd")

# 2.Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
#ANSWER:
def upper_lower_frequency(st):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  upper_count,lower_count = 0,0
  for char in st:
    if char in alpha:
      lower_count += 1
    elif char.lower() in alpha:
      upper_count += 1
  print("No. of Upper case characters :",upper_count)
  print("No. of Lower case characters :",lower_count)
#invoke the function
upper_lower_frequency("GEOFFThomas")
#OUTPUT:
# No. of Upper case characters : 6
# No. of Lower case characters : 5

# 3.Create a function that takes a list and returns a new list with unique elements of the first list.
#ANSWER:
def unique(l):
  return(list(set(l)))
print(unique([1,1,2,3,4,1,4,5,6,6]))#[1, 2, 3, 4, 5, 6]

# 4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#ANSWER:
def word_sort(seq):
  result = "-".join(sorted(seq.split("-")))
  print(result)#ant-elephant-giraffe-goat-zebra
word_sort("giraffe-goat-ant-zebra-elephant")

# 5.Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT
def capitalize():
  lines = []
  while True:
    line = input("Enter line by line or leave blank to exit:")
    if line:
      lines.append(line.upper())
    else:
      break
  for line in lines:
capitalize()
#OUTPUT:
# Enter line by line or leave blank to exit:Hello world
# Enter line by line or leave blank to exit:Practice makes perfect
# Enter line by line or leave blank to exit:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# 6.Define a function that can receive two integral numbers in string form and compute their sum and print it in console.
#ANSWER:
def string_sum(st1,st2):
  print(int(st1)+int(st2))#2558
string_sum("123","2435")

# 7.Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, 
#then the function should print all strings line by line.
#ANSWER:
def longest_string(st1,st2):
  length1, length2 = len(st1),len(st2)
  
  if length1 == length2:
    print(st1)
    print(st2)
  else:
    print(st1 if length1>length2 else st2)
longest_string("geoff","thomas")#thomas
longest_string("geoff","abcde")#geoff\n abcde 

# 8.Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20.
#ANSWER:
def square_tuple():
  t = []
  for num in range(2,20):
    t.append(num**2)
  print(tuple(t))#(4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361)
square_tuple()

# 9.Write a function called showNumbers that takes a parameter called limit. It should print all 
# the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
#ANSWER:
def showNumbers(limit):
  for number in range(limit+1):
    if number % 2 == 0:
      print(number," EVEN")
    else:
      print(number," ODD")
showNumbers(3)
#OUTPUT:
# 0  EVEN
# 1  ODD
# 2  EVEN
# 3  ODD

#10.Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
#ANSWER:

#11.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	 Use filter() to filter elements of a list
#        Use lambda to define anonymous functions
#ANSWER:
def make_list():
  given_list = range(1,11)
  squared_list = map(lambda x:x**2, given_list)
  even_squared_list = list(filter(lambda x:x % 2 == 0, squared_list))
  print(even_squared_list)#[4, 16, 36, 64, 100]
  # Perform the same in one line
  print(list(map(lambda x:x**2, filter(lambda x:x % 2 == 0, given_list))))#[4, 16, 36, 64, 100]
make_list()

# 12. 	Write a function to compute 5/0 and use try/except to catch the exceptions
#ANSWER:
def divisionbyZero():
  try:
    quotient = 5/0
  except:
    print("Division by zero")
divisionbyZero()
# This function try to run 5/0 but it fails and runs the except block

#13.Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 
from functools import reduce
def flatten_list(l):
  def helper(x, y):
      return x + y
  lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
  joinedlist = reduce(helper, lists)
  print(joinedlist)  # prints [1, 2, 3, 4, 5, 6, 7, 8]
  print(int("".join(str(i) for i in joinedlist[:-1])))#1234567
flatten_list([[1,2,3],[4,5],[6,7,8]])

#  14. 	What is the output of the following codes:
# (i) def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
#ANSWER:
2

# (ii) def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#     print('after f?')
# a()
#ANSWER:
after f
# After the finally it will throw an error as f() is not defined
# NameError: name 'f' is not defined
