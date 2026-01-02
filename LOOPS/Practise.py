# 1. Print numbers from 1 to 10 using a for loop.
# 2. Print even numbers between 1 and 50 using a for loop.
# 3. Print the sum of first 10 natural numbers using a while loop.
# 4. Print all numbers divisible by 5 from 1 to 100.
# 5. Print the multiplication table of a given number.
# 6. Count the digits in a given number using a while loop.
# 7. Print characters of a string one by one using a for loop.
# 8 .Print squares of numbers from 1 to 10.
#9. Count consonants in a string.
#10. Print each character of a string on a new line.
#11. Print the reverse of a string using a for loop.
# 12.Print all elements of a list using a for loop.
#13. Find the largest number in a list.
# 14.Find the smallest number in a list.
#15. Print the sum of all elements in a list.


# 1. Print numbers from 1 to 10 using a for loop.
for i in range(1,11): 
    print(i)

# 2. Print even numbers between 1 and 50 using a for loop.

for i in range(1,51):
    if i%2==0:
        print( i )

# 3. Print the sum of first 10 natural numbers using a while loop.
i = 1
total = 0
while i<10:
    total+=i
    i+=1
print(total)


# 4. Print all numbers divisible by 5 from 1 to 100.
for i in range(1,101):
    if i%5==0:
      print(i)



## 5. Print the multiplication table of a given number.
num = (int(input("Enter a number:")))
for i in range(1,11):
    print(num,"X",i,"=",num  * i )



# 6. Count the digits in a given number using a while loop.
num = int(input("Enter a number: "))

if num == 0:
    print("Number of digits: 1")
else:
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("Number of digits:", count)



#7)  Print characters of a string one by one using a for loop.
for ch in 'HELLO':
    print(ch)


# 8). Print squares of numbers from 1 to 10.
for i in range(1, 11):
    print("Square of", i, "is", i * i)

#9. Count vowels in a string.
S =(input(" Enter a string:"))
count =0
for ch in S:
    if ch in "aeiouAEIOU":
        count=count+1
print(count)

#10. Print each character of a string on a new line.
s= ("Enter a string:")
for ch in s:
    print(ch)

#11.  # Print the reverse of a string using a for loop.

s = input("Enter a string: ")

for ch in s[::-1]:
    print(ch, end="")

12. # Print all elements of a list using a for loop.

numbers = [10, 20, 30, 40, 50]

for item in numbers:
    print(item)

#13.# Find the largest number in a list.
numbers = [2,12,3,9,25,7]
largest = numbers[0]
for n in numbers:
    if n> largest:
        largest = n
print(largest)

 # 14.Find the smallest number in a list.
numbers = [5, 12, 3, 9, 25, 7]
smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print(smallest)

#15.. Print numbers from 10 down to 1 (reverse order).
for i in range(10,0,-1):
    print(i) 