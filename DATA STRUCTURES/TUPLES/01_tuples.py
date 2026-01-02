# a = (1,2,3,4)

# print(a)
# print(a[2])

# print(a.count(2))
# print(a.index(1 ))

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

list1 = [10, 20, 30, 40]
list2 = [5, 15, 25, 35]

mid1 = len(list1) // 2
mid2 = len(list2) // 2

print(list1[mid1-1], list1[mid1])
print(list2[mid2-1], list2[mid2])
