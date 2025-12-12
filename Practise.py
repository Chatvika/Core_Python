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

# 1).# Print numbers from 1 to 50 using a for-loop.

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

#9).# Print the index and value of each character in a string.
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