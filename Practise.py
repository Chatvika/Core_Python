# Basic:
# Print numbers from 1 to 50 using a for-loop.
# Print all multiples of 5 from 5 to 100.
# Print the characters of a string one by one.
# Count how many vowels are in a given string.
# Print the square of each number from 1 to 15.
# Print all elements of a list.
# Print numbers from 20 to 1 in reverse order.
# Print the sum of all numbers in a list.
# Print only odd numbers from 1 to 30.
# Print the index and value of each character in a string.


# Intermediate:
# Reverse a string using a for-loop.
# Find the largest number in a list.
# Find the second-largest number in a list.
# Count how many even and odd numbers are in a list.
# Print all substrings of a string using nested loops.
# Check if a string is a palindrome using a for-loop.
# Merge two lists using a for-loop.
# Find the factorial of a number using a for-loop.
# Create a new list containing squares of another list’s elements.
# Print a multiplication table for a given number.

#1) Print numbers from 1 to 50 using a for-loop.

for i in range(1,51):
    print(i)

#2).# Print all multiples of 5 from 5 to 100.

for i in range(5,101):
    if i%5==0:
        print(i)

        #or
for i in range(5,101,5):
    print(i)

#3).# Print the characters of a string one by one.

var ="How are you"
for i in var:
    print(i)

#4).# Count how many vowels are in a given string.

s = "Hello aeiow"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
     count+=1
print(count)

#5).# Print the square of each number from 1 to 15.

for i in range(1,16):
    print(i*i)

#6).# Print all elements of a list.

B =[10,20,30,40,50]
for xcvb in B: 
    print(xcvb)

#7).# Print numbers from 20 to 1 in reverse order.

for i in range(20,0,-1):
    print(i)


#8).# Print only odd numbers from 1 to 30.

for i in range(1,31):
    if i%2!=0:
        print(i)

# 9). Print the index and value of each character in a string.
s1 = "hey how do you do"
for index in range(len(s1)):
    print(index, s1 [index])



#10).# Reverse a string using a for-loop.
s =  "Python"
rev= ""
for ch in s:
     rev = ch + rev
print(rev)


#11).# Find the largest number in a list.
numbers = [10,20,30,86,104,96]
largest = numbers[0]
for num in numbers:
    if num> largest:
        largest = num

print("Largest number:",largest)

# 12). Find the second-largest number in a list.
numbers = [10,20,30,86,104,96]
largest = numbers[0]
for num in numbers:
    if num>largest:
        largest = num
numbers.sort() 
print(numbers[-2])

#13). # Count how many even and odd numbers are in a list.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
even_count=0
odd_count =0
for num in  numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)

## 14).Check if a string is a palindrome using a for-loop.
text = "Sir "
reverse_text =  ""
for ch in text:
    reverse_text = ch +reverse_text
if text == reverse_text:
        print("Palindrome")
else:
    print("Not a Palindrome")

##15).  Merge two lists using a for-loop.
list1 = [1,2,3]
list2 =[4,5,6]
merged_list =[]
for item in list1:
    merged_list.append(item)
for item in list2:
    merged_list.append(item)
print(merged_list)

#16).# Create a new list containing squares of another list’s elements.
numbers = [1,2,3,4,5]
squares= []
for n in numbers:
    squares.append(n*n)
print(numbers)
print(squares)

##17).  Print a multiplication table for a given number.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# More Basic-Level For-Loop Questions

# 1). #Print every third number from 1 to 30.
for i in range(1,31,3):
    print(i)

#2). Print the alphabet from A to Z using a loop.
for ch in range(ord('A'),ord('Z') + 1):
    print(chr(ch))

# 3). Print each element of a list along with "is processed".
numbers = [1,2,3,4,5]
for num in numbers:
    print(num , "is process")

#4). Print the cubes of numbers from 1 to 10.
for i in range(1,11):
    print(i**3)

#5). Count how many characters are in a string without using len().
var = "JAVA"
count = 0
for ch in var:
    count+=1
print(count)

#6).  Print all numbers divisible by 3 OR 7 from 1 to 100.
for i  in range(1,101):
    if i%3==0 or i%7==0:
        print(i)

    
#7). Print all positive numbers in a list (ignore negatives).
numbers = [10,-2,-3,9,-10,100]
for num in numbers:
    if num >0:
        print(num)

# 8).Convert each character of a string to uppercase manually using a loop.
text = "python"
result = ""

for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)

# 9). Count how many consonants are in a string.
text = "Python programing"
count = 0
vowels = "aeiouAEIOU"
for ch in text:
    if ch.isalpha() and ch not in vowels:
        count +=1
print(count)

#10).  Remove all zeros from a list using only loops.
numbers = [3,0,5,0,7,9,0,2]
new_list = []
for n in numbers:
    if n !=0:
        new_list.append(n)
print(new_list)

#11).  Count how many times each character appears in a string.
text = "banana"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)


# 12). Print all prime numbers from 1 to 100.
for num in range(2,101):
    is_prime = True
    for i in range(2,num):
        if num %i==0:
            is_prime= False
            break
    if is_prime:
        print(num)


#  13). print a right aligned star pattern  
#    *
#   **
#  ***
# ****

rows = 4

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)


#  14). Print a number pyramid like:
# 1
# 12
# 123
# 1234

rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# 15). Print all unique elements of a list (without using set).
numbers = [1,2,3,2,4,5,4,6,7,6,8,9,8,0]
unique =[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

# 16). Sort a list manually using two nested loops.
numbers = [5,2,8,1,3]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers [i] > numbers[j]:
            numbers [i],numbers[j] = numbers[j],numbers[i]
print("Sorted list:" , numbers)



# while loop

# 1. Print numbers from 1 to 10 using a while loop.
j = 1
while j<11:
    print(j) 
    j+=1

#.2).  Print all even numbers between 1 and 50 using a while loop.
i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1
# 3). Ask user to enter numbers repeatdly untill they enter "0" then stop.
num = int(input("Enter a number(o to stop):"))
while num !=0:
        print("You entered:",num)
        num = int(input("Enter a number (0 to stop:"))
print("Loop stoped")

# 4). Count how many times a while loop runs before a variable reaches a certain value.
count = 0
x = 0
while x<10:
     x+=1
     count+=1
print("loop ran",count,"times")

#5).  Print the sum of numbers from 1 to 100 using a while loop.
i = 1
total = 0
while i<=100:
     total += i
     i+=1
print("sum=",total)

# 6. Reverse the digits of an integer using a while loop.
num = int(input("enter a number:"))
reverse = 0
while  num > 0:
    digit = num %10
    reverse = reverse *10 +digit
    num = num//10
print("reversed number;" , reverse)

# 7. Keep asking the user for a password until they enter the correct one.
correct_password="Python123"
password = ""

while password != correct_password:
    password =input("Enter password:")
print("Access Granted")

# 8. Print a multiplication table (e.g., for 5) using a while loop.

num = 5
i = 1
while i <=10:
    print(num,"X",i,"=" ,num*i)
    i+=1  

#9.print the digits of a num one by one a while loop 
num = int(input("Enter a number:"))
while num >0:
    digit = num%10
    print(digit)
    num = num//10

# 10).  Keep doubling a number until it exceeds 1000; print how many doublings happened.

num = int(input("Enter a number:"))
count = 0
while num <= 1000:
    num= num*2
    count+=1
print("Number of doublings: ",count)

# intermidiate  while loop questions

#1). Find the factorial of a number using a while loop.

num = int(input("Enter a number: "))
fact =1
i = 1
while i<=num:
    fact = fact *i
    i+=1
print("factorial",fact)

# 2).Count how many digits are in a given number using a while loop. 
num =int(input("enter a number:"))
count =0
while num>0:
    count+=1
    num=num//10
print(count)

# 3). 
num = int(input("Enter a number:"))
temp = num
rev = 0
while temp >0:
    digit = temp %10
    rev = rev*10+digittemp = temp//10
if num==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# 4).Find the sum of digits of a number using a while loop.
num = int(input("enter a number:"))
sum_digits= 0
while num>0:
    digit = num%10
    sum_digit=sum_digits +digit
    num = num//10
print("Sum of Digits:",sum_digit)

#5).  Print all prime numbers between 1 and 100 using a while loop.

num = 2
while num <=100:
    i=2
    while i <num:
        if num%i==0:
            break
        i+=1
    if i ==num:
        print(num)
    num+=1
# 6). Generate the Fibonacci series up to n terms using a while loop.
n= int(input("Enter a num of terms:"))
a,b = 0,1
count = 0
while count <n:
    print(a,end="")
    a,b =b , a+b
    count+=1

# 7).Keep taking numbers from the user until the sum exceeds 100.
total = 0
while total <=100:
     num =int(input("Enter a number:"))
     total+=num
print("Sum exceeded 100")
# 8).Find the greatest common divisor (GCD) of two numbers using a while loop.

a = int(input("Enter first number:"))
b = int(input("Enter  second number:"))
while b!=0:
    a,b=b , a%b
print("GCD = ",a)

# 9).Print all divisors of a given number using a while loop.
n=int(input("Enter a number:"))
i=1
while i<=n:
    if n %i==0:
        print(i)
    i+=1

    # adv - while loop questions

#1). Reverse a string using a while loop (without slicing).
s = input("Enter a string: ")

i = len(s) - 1
rev = ""

while i >= 0:
    rev += s[i]
    i -= 1

print("Reversed string:", rev)
# 2). Check if a number is an Armstrong number using a while loop
n = int(input("Enter a number: "))

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# 3). Convert a decimal number to binary using a while loop.
n = int(input("Enter a decimal number: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary number:", binary)


# 4).Count vowels and consonants in a string using a while loop.
s = (input("Enter a string:")).lower()
vowels = 0
consonents=0
i = 0
while i < len(s):
    if s[i].isalpha():
        if s[i] in 'aeiou':
            vowels+=1
        else:
            consonents+=1
    i+=1
print("Vowels" , vowels)
print("Consonents" , consonents)

# 5)/Simulate an ATM system (balance, withdraw, deposit) using a while loop.

balance = 1000
choice = 0
while choice != 4:
    print("\n----ATM MENU----")
    print("1.check balance")
    print("2.deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice==1:
        print("Your balnc is :" , balance)

    elif choice ==2:
        amount = int(input("Enter amount to deposit:"))
        if amount > 0:
            balance +=amount
            print("Deposited Succussful")
        else:
            print("Invalid amount")
    elif choice==3:
        amount =int(input("Enter amount to withdraw:"))
        if amount >balance:
                print("Insufficient balance")
        elif amount<=0:
                print("invalid amount")
        else:
            balance-=amount
            print("collect your cash")
    elif choice ==4:
        print("Thank you for using ATM")
    else:
        print("Invalid choice ,try again")

# 6).Find the least common multiple (LCM) of two numbers using a while loop.
num1 =int(input("Enter first number: "))
num2 =int(input("Enter a second number:"))
lcm = num1 if num1>num2 else num2
while True:
    if lcm % num1 ==0 and lcm % num2==0:
        print("LCM is",lcm)
        break
    lcm+=1

# 7). Implement a number guessing game using a while loop.
secret_number=7
guess=0
while guess!=secret_number:
    guess=int(input("Guess the num:"))
    if guess <secret_number:
        print("Too low! try again")
    elif guess >secret_number:
        print("too high !try again")
    else:
        print("Congratulations! you guessed the correct number.")

#8). Keep asking the user for numbers and store only unique values using a while loop.
unique_numbers=[]
num =None
while num!=0:
    num=int(input("Enter a number(0 to stop):"))
    if num==9:
        break
    if num not in unique_numbers:
        unique_numbers.append(num)
    else:
        print("Duplicate number,not defined")
print("Unique numbers enterd :",unique_numbers) 
#9).  Print a pyramid pattern using a while loop.
n = 4
i = 1

while i <= n:
    spaces = n - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)
    i += 1
# reverse a string
s="hello"
rev=s[::-1]
print("Reverse str:",rev)

# 2). check if numberis even or odd
n=12
if n%2==0:
    print("Even number")
else:
    print("Odd number")

# 3).find the factorial of a number
n=int(input("Enter a number:"))
fact = 1
for i in range(1,n+1):
    fact=fact*i
print("Factorial:",fact)

# 4).check if num is prime
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("not prime")

# 5).find the largest number in list
n=[1,2,3,4,5]
largest=n[0]
for i in n:
    if i > largest:
        largest=i
print(largest)

# 6).count vowels in string
s="Chatvika"
vowels="aeiouAEIOU"
count=0
for ch in s:
    if ch in vowels:
        count+=1
print(count)

# 7).check if str is a palindrome
s="Chatvika"
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 8).sum of elements in list
lst=[1,2,3,4,5]
total=0
for i in lst:
    total+=i
print(total)

# 9). Find the frequency of characters in a string
s=input("Enter a string:")
for ch in s:
    print(ch,":",s.count(ch))

# 10)Swap two numbers without using a third variable
a=10
b=50
a,b=b,a
print("a=",a)
print("b=",b)

s="CHATVIKA"
print(s.lower())
print(s[2:5]) 
