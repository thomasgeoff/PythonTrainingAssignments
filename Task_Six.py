# TASK SIX: CLASSES AND OBJECTS
# 1.	Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
#ANSWER:
def formula():
  C,H = 50,30
  seq = input("Enter the sequence: ")
  for D in seq.split(","):
    D = int(D)
    Q = ((2*C*D)/H)**0.5
    print("For %d, Q= %0.2f" % (D,Q))
formula()
# OUTPUT:
# Enter the sequence: 1,2,3,4,5
# For 1, Q= 1.83
# For 2, Q= 2.58
# For 3, Q= 3.16
# For 4, Q= 3.65
# For 5, Q= 4.08

# 2.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length
# as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 
# by default.
#ANSWER:
class Shape():
  def __init__(self):
    pass
  def area(self):
    return 0
class Square(Shape):
  def __init__(self,length):
    self.length = length
  def square_area(self):
    return self.length**2
#Create an object for square 
s = Square(5) 
#print square area
print(s.square_area())#25
#print shape area
print(s.area())#0

# 3.Create a class to find the three elements that sum to zero from a set of n real numbers.
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Output: [[-10,2,8],[-7,-3,10]]
#ANSWER:
class Solution:
  def search_triplets(self,arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
      if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
        continue
      self.search_pair(arr, -arr[i], i+1, triplets)
    return triplets

  def search_pair(self,arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
      current_sum = arr[left] + arr[right]
      if current_sum == target_sum:  # found the triplet
        triplets.append([-target_sum, arr[left], arr[right]])
        left += 1
        right -= 1
        while left < right and arr[left] == arr[left - 1]:
          left += 1  # skip same element to avoid duplicate triplets
        while left < right and arr[right] == arr[right + 1]:
          right -= 1  # skip same element to avoid duplicate triplets
      elif target_sum > current_sum:
        left += 1  # we need a pair with a bigger sum
      else:
        right -= 1  # we need a pair with a smaller sum
s = Solution()
print(s.search_triplets([-25,-10,-7,-3,2,4,8,10]))
#OUTPUT:
#[[-10, 2, 8], [-7, -3, 10]]

# 4.What is the output of the following code? Explain your answer as well.
# class Test:
#     def __init__(self):
#       self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#       self.y = 1
# def main():
#     b = Derived_Test()
#     print(b.y)
#     print(b.x,b.y)
# main()
#ANSWER: 
# It will throw an AttributeError as Derived_Test object has no attribute 'x'

# class A:
#     def __init__(self, x= 1):
#         self.x = x
# class der(A):
#     def __init__(self,y = 2):
#         super().__init__()
#         self.y = y
# def main():
#     obj = der()
#     print(obj.x, obj.y)
# main()
#ANSWER: 
#It will throw syntax error at main() call

# class A:
#     def __init__(self,x):
#         self.x = x
#     def count(self,x):
#         self.x = self.x+1
# class B(A):
#     def __init__(self, y=0):
#         A.__init__(self, 3)
#         self.y = y
#     def count(self):
#         self.y += 1     
# def main():
#     obj = B()
#     obj.count()
#     print(obj.x, obj.y)
# main()
#ANSWER: 
#3 1
 
# class A:
#     def __init__(self):
#         self.multiply(15)
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 4 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def multiply(self, i):
#         self.i = 2 * i;
# obj = B()
#ANSWER:
#30
 
# 5.	Create a Time class and initialize it with hours and minutes.
# Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Make a method displayTime which should print the time.
# Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
#ANSWER:
class Time:
  def __init__(self,hours,minutes):
    self.hours = hours
    self.minutes = minutes
  def addTime(self,a,b):
    hrs = a.hours+b.hours+(a.minutes+b.minutes)//60
    mins = (a.minutes+b.minutes)%60
    print("%d hour and %d min" %(hrs,mins))
  def displayTime(self):
    print("%d hour and %d min" %(self.hours,self.minutes))
  def displayMinute(self):
    totalMins = self.hours*60 + self.minutes
    print("Total Minutes=",totalMins)
t1 = Time(2,50)
t1.displayTime()
t2 = Time(1,20)
t2.displayTime()
t1.addTime(t1,t2)
t3 = Time(1,2)
t3.displayMinute()
# OUTPUT:
# 2 hour and 50 min
# 1 hour and 20 min
# 4 hour and 10 min
# Total Minutes= 62

# 6. Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. 
# The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as,
#  the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following 
#  instance methods:
# yearPasses() should increase the  instance variable by .
# amIOld() should perform the following conditional actions:
# If , print You are young..
# If  and , print You are a teenager..
# Otherwise, print You are old..	
# Sample Input:
# 4
# -1
# 10
# 16
# 18
# Sample Output:
# Age is not valid, setting age to 0.
# You are young.
# You are young.
 
# You are young.
# You are a teenager.
 
# You are a teenager.
# You are old.
 
# You are old.
# You are old.
#ANSWER:
class Person():
  def __init__(self,age):
    if age < 0:
      print("Age is not valid, setting age to 0")
      self.age = 0
    else:
      self.age = age
  def yearPasses(self):
    self.age += 1
  def amIOld(self):
    if self.age<13:
        print('You are young.')
    elif self.age>=13 and self.age<18:
        print('You are a teenager.')
    else:
        print('You are old.')
t = int(input("Enter the number of input:"))
for i in range(0, t):
    age = int(input("Enter the age:"))         
    p = Person(age)  
    p.amIOld()
    print("After 3 years")
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
#OUTPUT:
# Enter the number of input:4
# Enter the age:-1
# Age is not valid, setting age to 0
# You are young.
# After 3 years
# You are young.

# Enter the age:10
# You are young.
# After 3 years
# You are a teenager.

# Enter the age:16
# You are a teenager.
# After 3 years
# You are old.

# Enter the age:18
# You are old.
# After 3 years
# You are old.
