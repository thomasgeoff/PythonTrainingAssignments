# TASK TWO: OPERATORS AND DECISION MAKING STATEMENT

#Q1.Write a program in Python to perform the following operation:
#   If a number is divisible by 3 it should print “Consultadd” as a string
#   If a number is divisible by 5 it should print “c” as a string
#   If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
#ANSWER:
def divisiblityCheck(number):
  if number % 3 == 0 and number % 5 == 0:
    print("Consultadd Python Training")
  elif number % 3 == 0:
    print("Consultadd")
  elif number % 5 == 0:
    print("c")
#invoke the function
divisiblityCheck(3)#Consultadd
divisiblityCheck(5)#c
divisiblityCheck(15)#Consultadd Python Training

# Q2.Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition 
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
# Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose 
# an option 5.
# At the end if the answer of any operation is Negative print a statement saying “zsa”
# NOTE: At a time user can perform one action at a time.
#ANSWER:
def calculate(operation, num1, num2, num3=0, num4=0):
  if operation == 1:
    result = num1 + num2
  elif operation == 2:
    result = num1 - num2
  elif operation == 3:
    result = num1 / num2
  elif operation == 4:
    result = num1 * num2
  elif operation == 5:
    result = (num1 + num2 + num3 +num4)/4
    
  if result < 0:
    print("zsa")
  return result 

if __name__ == "__main__":
  
  continue_flag = 'y'
  while continue_flag == 'y':
    first = int(input("Enter the first number:"))
    second = int(input("Enter the second number:"))
    operation = int(input("Enter the operation(1,2,3,4,5) to perform:"))
    
    if 0<operation<=5:
      if operation != 5:
        print(calculate(operation, first, second))
      else:
        first1 = int(input("Enter the first1 number:"))
        second2 = int(input("Enter the second2 number:"))
        print(calculate(operation, first, second,first1, second2))
    else:
      print("Invalid input for operation")
    
    continue_flag = input("Do you want to continue[y/n]:")
    
#Q3.Write a program in Python to implement the given flowchart:
#ANSWER:	
def flowchart():
  a,b,c = 10,20,30
  avg = (a+b+c)/3
  print("avg =",avg)
  
  if avg > a and avg > b and avg > c:
    print("avg is higher than a,b,c")
  else:
    if avg > a and avg > b:
      print("avg is higher than a,b")
    else:
      if avg > a and avg > c:
        print("avg is higher than a,c")
      else:
        if avg > b and avg > c:
          print("avg is higher than b,c")
        else:
          if avg > a:
            print("avg is just higher than a")
          else:
            if avg > b:
              print("avg is just higher than b")
            else:
              if avg > c:
                print("avg is just higher than c")
#Output:
# avg = 20.0
# avg is just higher than a 

#Q4.Write a program in Python to break and continue if the following cases occurs:
#   If user enters a negative number just break the loop and print “It’s Over”
#   If user enters a positive number just continue in the loop and print “Good Going”
#ANSWER:
def break_continue():
  
  while True:
    number = int(input("Enter the first number:"))
    if number > 0:
      print("Good Going")
      continue
    break 
  print("It's Over")
#invoke the function 
break_continue() 

#Q5.Write a program in Python which will find all such numbers which are divisible by 7
#   but are not a multiple of 5, between 2000 and 3200.
#ANSWER:
def divisibleby7andnot5():
  result = []
  for number in range(2001,3200):
    if number % 7 == 0 and number % 5 != 0:
      result.append(number)
  return result
#invoke the function
print(divisibleby7andnot5())
 
#Q6.What is the output of the following code examples?
#x=123 
#for i in x:
#	print(i)
#ANSWER:
It will result in Type error as the variable x is an integer and not an iterable

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(“error”)
#ANSWER:
0
1
2

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break
#ANSWER:
0
1
2
3
4

#Q7.Write a program that prints all the numbers from 0 to 6 except 3 and 6.
#   Expected output: 0 1 2 4 5
#   Note: Use ‘continue’ statement
def printnumber():
  
  for number in range(0,7):
    if number != 6 and number != 3:
      print(number, end =" ")
      
# Q8.Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#    Expected output: consul12
#      Letters 6
#      Digits 2
#ANSWER:
def digits_letter():
  digit_count,letter_count = 0,0
  string_input = input("Enter a string:")
  for char in string_input:
    if char.isdigit():
      digit_count += 1
    elif char.isalpha():
      letter_count += 1
  print("Letters ",letter_count)
  print("Digits ",digit_count)
  
#Q9.Read the two parts of the question below: 
#   Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program 
#   stops, otherwise it continues forever. 
#ANSWER:
def guessthenumber(luckynumber):
  
  while True:
    user_input = int(input("Guess the number:"))
    if user_input == luckynumber:
      print("Your guess is right")
      break
    else:
      print("Your guess is wrong")
#invoke the function    
guessthenumber(10)
  
# Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ 
# for the number and ‘answer’ for the answer to the question whether they want to continue guessing. 
# The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as 
# a user has not answered “no” and has not guessed the correct number)
#ANSWER:
def guessthenumber(luckynumber):
  
  answer = "yes"
  while answer.lower() == "yes":
    number = int(input("Guess the number:"))
    if number == luckynumber:
      print("Your guess is right")
      break
    print("Your guess is wrong")
    answer = input("Do you want to continue[yes/no]:")
#invoke the function    
guessthenumber(10)


#Q10.Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#            		counter=1
# 		While counter <= 5:
# 			print(“Type in the”, counter, “number”
# 			counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct 
# number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth 
# guess it stops and prints “Game over!”.
#ANSWER:
def guessthenumber(luckynumber):
  
  counter = 1
  while counter <= 5:
    number = int(input("Guess the number:"))
    if number == luckynumber:
      print("Good guess!")
    else:
      print("Try again")
    counter += 1
  print("Game over!")
#invoke the function   
guessthenumber(10)

# Q11.In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate 
#     the while loop so that users do not have to continue guessing after they found the number. If the user does 
#     not guess the number at all, print “Sorry but that was not very successful”.
#ANSWER:
def guessthenumber(luckynumber):
  guessedRight = False
  counter = 1
  while counter <= 5:
    number = int(input("Guess the number:"))
    if number == luckynumber:
      print("Good guess!")
      guessedRight = True
      break
    else:
      print("Try again")
    counter += 1
  if not guessedRight:
    print("Sorry but that was not very successful")
  print("Game over!")
#invoke the function    
guessthenumber(10)
