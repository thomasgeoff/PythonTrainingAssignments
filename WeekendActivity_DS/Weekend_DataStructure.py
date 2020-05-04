# WEEKEND ACTIVITY ON DATA STRUCTURES

#1.Create a list of the 10 elements of four different types of Data Types like int, string, complex and float.
#ANSWER:
l = [1,2.12,"geoff",2+3j,5,6.0,"GT",2,1,3]
print(len(l))#10

#2.Create a list of size 5 and execute the slicing structure 
#ANSWER:
l = [1,2,3,4,5]
print(l[:])#[1,2,3,4,5]
print(l[0:5])#[1,2,3,4,5]

#3.Create a list of given structure and run 
#ANSWER:
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
print(x[5][:4])
# Access list [600,  700]
print(x[6:8])
# Access list [100, 300, 500, 600, 800]
print([x[i] for i in range(len(x)) if i % 2 == 0])
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])
# Access list [10]
print(x[5][5][:1])
# Access list [ ]
print(x[:0])

#4.Create a list of thousand number using range and xrange and see the difference between each other.
#ANSWER:
list_with_range = [ i for i in range(1,1001)]
print(type(list_with_range))# returns a list which is iterable
list_with_xrange = [ i for i in xrange(1,1001)]
print(type(list_with_xrange))# returns a xrange object which is just used for the looping

#5.How Tuple is beneficial as compare to the list?
#ANSWER:
# Tuple uses less memory. Thus indexing speed is faster compared to list.
# Unlike lists, tuple can be used as keys in a python dictionary

#6.Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
#ANSWER:
def divisiblebyTwoThree():
  for number in range(1,101):
    if number % 3 == 0 and number % 2 == 0:
      print(number)
      
#7.Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.
#ANSWER:
def reverse_vowel(st):
  reversed_string = st[::-1]
  for index,char in enumerate(reversed_string):
    if char.lower() in ['a','e','i','o','u']:
      print(char,":",index)
#invoke the function
reverse_vowel("GEOFF")
#OUTPUT:
# O : 2
# E : 3
  
# 8. 	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.
#ANSWER:
def even_word(st):
  
  for word in st.split():
    if len(word) % 2 == 0:
      print(word)
# invoke the function
even_word("hello my name is abcde")
#OUTPUT:
# my
# name
# is

# 9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]
#ANSWER:
def twosum(l,target):
  seen = {}
  for index,number in enumerate(l):
    if number in seen:
      print(number,l[seen[number]])
    else:
      seen[target-number] = index
# invoke the function
twosum([1,2,3,4,5,6,7,8,9,-1],8) 
#OUTPUT:
# 5 3
# 6 2
# 7 1
# -1 9
 
# 10. 	Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.
#ANSWER:
def even_odd_list():
  even_list = [None]*5
  odd_list = [None]*5
  even_index,odd_index = 0,0
  
  while not(even_index == 5 and odd_index == 5):
    user_input = int(input("Enter a number in the range of 1,50:"))
    if user_input % 2 == 0:
      if even_index < 5:
        even_list[even_index] = user_input
        even_index += 1
    else:
      if odd_index < 5:
        odd_list[odd_index] = user_input
        odd_index += 1
  print("Sum of even list %s : %d " %(even_list,sum(even_list)))
  print("Sum of odd list %s : %d " %(odd_list,sum(odd_list)))
#invoke the function
even_odd_list()
#OUTPUT:
# Enter a number in the range of 1,50:2
# Enter a number in the range of 1,50:1
# Enter a number in the range of 1,50:4
# Enter a number in the range of 1,50:6
# Enter a number in the range of 1,50:8
# Enter a number in the range of 1,50:10
# Enter a number in the range of 1,50:12
# Enter a number in the range of 1,50:3
# Enter a number in the range of 1,50:14
# Enter a number in the range of 1,50:16
# Enter a number in the range of 1,50:5
# Enter a number in the range of 1,50:7
# Enter a number in the range of 1,50:9
# Sum of even list [2, 4, 6, 8, 10] : 30 
# Sum of odd list [1, 3, 5, 7, 9] : 25 
        
# 11.Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab  
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
#ANSWER:
def char_frequency(st):
  count = {}
  for i in st:
    if i.isalpha():
      count[i] = count.get(i,0)+1
  for key,val in count.items():
    print("%s=%d" % (key,val),end=" ")
#invoke the function
char_frequency("12abcbacbaba344ab")
#OUTPUT:
#a=5 b=5 c=2

# 12.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
#ANSWER:
t = (1,2,3,4,5,6,7,8,9,10)
temp = []
for number in t:
  if number % 2 == 0:
    temp.append(number)
print(tuple(temp))#(2, 4, 6, 8, 10)