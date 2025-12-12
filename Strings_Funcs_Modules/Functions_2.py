# Function: A function is a block of code written to perform a specific task. It is reusable and helps reduce repetition.
#greet("Chatvika")

# #4).Variable-Length Arguments : *args → multiple values
#                                **kwargs → multiple keyword values
def add(*nums):
     print(sum(nums))

def info(**data):
     print(data)


x = 10   # global

def show():
     global x
     x = 20

show()
print(x)   # 20
#Print all even numbers from 2 to 20.
for i in range(1,21):
 if i%2==0:
    print(i)
#Compute the sum of the first 10 natural numbers using a for-loop.
#Print each character of a string using a for-loop.
# for char in "Hello":
#    print(char)


var = "Chatvika"
for i in var:
   print(i)
#Count how many vowels are in a given string.

s1= "Hi How are U"
s2="aeiouAEIOU"
for i in s1:
    if i in s2:
        print(i)