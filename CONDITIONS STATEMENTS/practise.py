#  #1).Write a program that checks if a number is positive.''

n = int(input("Enter a number: "))
 
if n>0:
     print("Positive number")




# #2). Check if num is even or odd

x = int(input("Enter a number:"))
if x % 2==0:
     print("Even number")
else:
     print("odd number")




# #3) Check if a user-entered age makes them eligible to vote (18+).

age = int(input("Enter a number:"))
if age>18:
  print("You are ELigible to Vote")
else:
    print("Your not eligible to vote")

   

# #4).Determine whether a character is a vowel or consonant

ch =input("Enter a letter :")
if ch in ("a","e","i","o","u","A","E","I","O","U"):
   print("vowel")
else:
   print("Consonent")

# #5).Check if a number is divisible by 5

x=int(input("Enter a number:"))
if x%5==0:
   print("divisible by 5")
else:
   print("Not divisible by 5")
 
 

# #6).Compare two numbers and print the larger one.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
     print("Larger number is:", a)
else:
     print("Larger number is:", b)


# #7).Check if a number is between 1 and 100.

num = int(input("Enter a number: "))
if num >= 1 and num <= 100:
     print("The number is between 1 and 100.")
else:
     print("The number is NOT between 1 and 100.")


# #8).determine if a string contain the letter "A"

s = input("Enter a string:")
if 'a'in s:
    print("the string contain letter 'a'.")
else:
    print("The string does not contain letter 'a'.")

 #9). MUltiple both 3and 7
  
num = int(input("Enter a number: "))

# # Check if divisible by both 3 and 7
if num % 3 == 0 and num % 7 == 0:
     print(f"{num} is a multiple of both 3 and 7.")
else:
     print(f"{num} is NOT a multiple of both 3 and 7.")

# #10). Write a program that checks if a given year is a leap year.

year = int(input("Enter a year:"))
if (year % 400 == 0):
     print("{year} is a leap year.")
else:
     print("{year}is not a leap year.")

# #11).Determine if a number is positive, negative, or zero.

num = float(input("Enter a number:"))
if num>0:
     print("The number is positive")
elif num<0:
     print("the number is negative")
else:
     print("The number is zero.")

# #12).Check if a password is at least 8 characters long.

password = input("Enter your password:")
if len(password) >=8 :
     print("The Password is Strong enough")
else:
     print("The Password istoo short,must be 8 char ")

# #13).Check if a temperature is above, below, or equal to freezing point (0°C).

temperature =float(input("Enter  temperature:"))
if temperature>0 :
     print("The temperature is abovefreezing point.")
elif temperature<0 :
     print("The temperature is below freezing point:")
else :
     print("the temperature is at freezing point:") 


# #14).  Check whether a number has exactly 3 digits. 
#  
num = input("Enter a number: ")
if len(num) == 3:
     print("The number has exactly 3 digits.")
else:
     print("The number does not have exactly 3 digits.") 


# #15). Determine if a student passed based on a score (>= 50).

score = int(input("Enter a student score."))
if score>=50:
     print("Pass")
else:
     print("Fail")

# #16).Check if a person qualifies for a senior discount (age 60+).

age = int(input("Enter age."))
if age>=60:
     print("Eligible for senior discount.")
else:
     print("Not eligible for senior discount")

# #17).Determine if two strings are equal ignoring case.

str1 =input("Enter a first string:")
str2 =input("Enter a second string:")
if str1.lower()==str2.lower():
  print("Strings are equal(ignoring case)")
else:
     print("Strings are not equal.")

 #18).Check if a number is in a given list.

numbers = [10,20,30,40]
n = int(input("Enter a number:"))
if n in numbers:
     print("Number is in given list.")
else:
     print("Number is not in given list.")

 #19).Check if three numbers form a triangle (triangle inequality).
 
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
     print("These sides form a Triangle")
else:
     print("These sides do NOT form a Triangle")
#20.)Check if a number is prime (simple method: count divisors).

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
     if num % i == 0:
        count += 1

if count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")

