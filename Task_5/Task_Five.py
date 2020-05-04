# TASK FIVE: FILE HANDLING AND EXCEPTION HANDLING

# 1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError
#ANSWER:
def syntax_exception():
  try:
    print(eval('six times seven'))
  except SyntaxError:
    print ('Syntax error found')
syntax_exception()
#OUTPUT:
#Syntax error found

# 2. 	Write a program in Python to allow user to open a file by using argv module. If the entered name is 
# incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode. 
#ANSWER:
import sys
script, filename = sys.argv
while True:
    try:
        txt = open(filename,"r")
        print("The filename exists:",filename)
        break
    except IOError as E:
        print('File Not Found')
        print("Enter the file name")
        filename = input("Enter the filename:")
txt.close()

# 3. 	Write a program to handle an error if the user entered the number more than four digits it should 
# return “Please length is too short/long !!! Please provide only four digits” 
#ANSWER:
def fourdigit_number():
  while True:
    try:
      number = int(input("Enter a number:"))
    except ValueError:
      print ('Invalid input')
    if len(str(number)) != 4:
      print("Please length is too short/long !!! Please provide only four digits")
    else:
      print("Valid Input")
      break
fourdigit_number()
#OUTPUT:
# Enter a number:12
# Please length is too short/long !!! Please provide only four digits
# Enter a number:12345
# Please length is too short/long !!! Please provide only four digits
# Enter a number:1234
# Valid Input

# 4. 	Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type 
# Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
#ANSWER:
def login_page():
  counter = 0
  while True:
    try:
      username = input("Enter username: ")
      password = input("Enter password: ")
    except ValueError:
      print ('Invalid input')
    counter += 1
    if not(username == "thomasgeoff" and password == "password"):
      print("Invalid Credentials")
      if counter > 2:
        print("You have attempted too many times")
        break
    else:
      print("Logged In")
      break
login_page()
#OUTPUT:
# Enter username: gt
# Enter password: pass
# Invalid Credentials
# Enter username: geoff
# Enter password: passw
# Invalid Credentials
# Enter username: geoff
# Enter password: password
# Invalid Credentials
# You have attmpted too many times
# Enter username: thomasgeoff
# Enter password: password
# Logged In

# 5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand 
# Finally and Raise concept.
#ANSWER:
# Finally 
# In Python we can have an optional finally clause in the try/exception blockand will be executed no matter what.
# One of its use is to release external resources.
# Raise
# Exceptions are at run time, but using the raise keyword we can forcefully raise it before running

# 6. 	Read any file using Python File handling concept and return only the even length string from the doc.txt file.
# Consider the content as: 
# 	Hello I am a file 
# 	Where you need to return the data string 
# 	Which is of even length 
# 	Make sure you return the content in 
# 	The same link as it is present.
#ANSWER:
with open("doc.txt") as file_handler:
    for line in file_handler.readlines():  
      if len(line.strip()) % 2 == 0:
        print(line.strip())
file_read.close()