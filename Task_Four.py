# TASK FOUR: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION AND DECORATOR
# 1.	Write a program to Python find the values which is not divisible 3 but is should be a 
# multiple of 7. Make sure to use only higher order function.
#ANSWER:
def main(l):
  for number in l:
    if number % 3 != 0 and number % 7 == 0:
      print(number)
main([i for i in range(1,11)])
#OUTPUT:
#7

# 2. 	Write a program in Python to multiple the element of list by itself using a traditional 
# function and pass the function to map to complete the operation.
# ANSWER:
def multiply(number):
  return number*number
print(list(map(multiply,range(1,6))))#[1, 4, 9, 16, 25]

# 3. 	Write a program to Python find out the character in a string which is uppercase using list comprehension.
# ANSWER:
result = [(char,True) for char in "GeoFf" if char not in "abcdefghijklmnopqrstuvwxyz"]
print(result)#[('G', True), ('F', True)]

# 4. 	Write a program to construct a dictionary from the two lists containing the names of students and their 
# corresponding subjects. The dictionary should maps the students with their respective subjects. 
# Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
# Student = ['Smit', 'Jaya', 'Rayyan']
# capital = ['CSE', 'Networking', 'Operating System']
# ANSWER:
student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']
# using dictionary comprehension
result = {student[i]:capital[i] for i in range(len(student))}
print(result)#{'Smit': 'CSE', 'Jaya': 'Networking', 'Rayyan': 'Operating System'}
# using zip
result = dict(zip(student,capital))
print(result)#{'Smit': 'CSE', 'Jaya': 'Networking', 'Rayyan': 'Operating System'}

# 5. 	Learn More about Yield, next and Generators
# ANSWER:
A Python generator is a function which return a generator object using the yield keyword 
and next() is used to move to the next value in the generator object

# 6. 	Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
# ANSWER:
def generator(st):
  for i in range(len(st)-1,-1,-1):
    yield st[i]
def reverse(st):
  print("".join(char for char in generator(st)))#edcba
reverse("abcde")

# 7. 	Write any example on decorators.
# ANSWER:
def new_decorator(original_function):
  def wrap_function():
    print("Decorations before the original function")
    original_function()
    print("Decorations after the original function")
  return wrap_function

def to_be_decorated():
  print("I want to be decorated!")

decorate = new_decorator(to_be_decorated)
decorate()
#Output:
# Decorations before the original function
# I want to be decorated!
# Decorations after the original function

#Decorator example
@new_decorator
def to_be_decorated_again():
  print("I want to be decorated again!")
to_be_decorated_again()
# OUTPUT:
# Decorations before the original function
# I want to be decorated again!
# Decorations after the original function

# 8. 	Learn about What is FRONT END and its Technologies and Tools
# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mentioned the name of companies using those 5 technologies individually
# ANSWER: 
1. React.js - used by Dropbox, PayPal, Pinterest, Facebook, Instagram
2. Ruby on rails - used by AirBnB, Twitter, SoundCloud, Shopify,Kickstarter.
3. Angular.js - used by Google, Upwork, Sony, General Motors, HBO
4. Vue.js - used by Xiaomi, Alibaba, Gitlab, Laracasts, Reuters
5. Django - used by Instagram, Pinterest, Udemy, Coursera, Robinhood
# Reference:
# https://dev.to/duomly/the-best-front-end-framework-to-learn-in-2019-dn7
# https://hotframeworks.com/frameworks