# TASK THREE: DATA STRUCTURES
#Q1.Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
#ANSWER: 
l = [1,2.12,"geoff",2+3j,5,6.0,"GT",2,1,3]
print(len(l))#10

#Q2.Create a list of size 5 and execute the slicing structure 
#ANSWER:
l = [1,2,3,4,5]
print(l[:])#[1,2,3,4,5]
print(l[0:5])#[1,2,3,4,5]

#Q3.Write a program to get the sum and multiply of all the items in a given list.
#ANSWER:
def listSumProduct(l):
  sums,product = 0,1
  for item in l:
    sums += item
    product *= item
  print("Sum = ",sums)
  print("Product = ",product)
#invoke the function
listSumProduct([1,2,3,4,5])
#OUTPUT:
# Sum = 15
# Product = 120

#Q4.Find the largest and smallest number from a given list.
#ANSWER:
def listMinMax(l):
  print("largest = %d and smallest = % d" %(max(l),min(l)))
#invoke the function
listMinMax([1,2,3,4,5])
#OUTPUT:
# largest = 5 and smallest = 1

#Q5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 
#ANSWER:
def new_list(l):
  result = []
  for item in l:
    if not item % 2 == 0:
      result.append(item)
  print(result)
#invoke the function
new_list([1,2,3,4,5,6,7,8,9,10])
#OUTPUT:
#[1, 3, 5, 7, 9]

#Q6.Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
#ANSWER:
def create_list():
  result = []
  for number in range(1,31):
    if number < 6 or number > 25:
      result.append(number*number)
  print(result)
#invoke the function
create_list()
#OUTPUT:
#[1, 4, 9, 16, 25, 676, 729, 784, 841, 900]

#Q7.Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]
#ANSWER:
def replace_list_element(l):
  print(l[0][:-1]+l[1])
#invoke the function
replace_list_element([[1,3,5,7,9,10],[2,4,6,8]])
#OUTPUT:
#[1,3,5,7,9,2,4,6,8]

# 8.	Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}
#ANSWER:
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)#{1:10,2:20,3:30,4:40}

# 9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}
#ANSWER:
n = 5
d = { x:x*x for x in range(1,n+1)}
print(d)#{1:1,2:4,3:9,4:16,5:25}

# 10. 	Write a program which accepts a sequence of comma-separated numbers from console and generate a list 
#and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)
#ANSWER:
def sequence():
  seq = input("Enter the sequence:")
  l = seq.split(",")
  t = tuple(l)
  print(l)
  print(t)
#invoke the function
sequence()
#OUTPUT:
# Enter the sequence:34,67,55,33,12,98
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')