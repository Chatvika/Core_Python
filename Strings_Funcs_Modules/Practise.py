# Write a function to print "Python is easy".

# Write a function that accepts two numbers and returns their sum.

# Write a function that checks if a number is positive, negative, or zero.

# Write a function that returns the length of a string without using len().

# Write a function that prints all items of a list.

# Write a function that returns the cube of a number.

# Write a function that takes a list and returns the maximum value.

# Write a function that counts how many even numbers are in a list.

# Write a function that accepts a name and prints a greeting message.

# Write a function that returns the reverse of a list.

#1).
def message():
    print("Python is easy")
message()


#2).
def add(a, b):
    print(a+b)
add(5,3)


#3).
def check_number(num):
    if num> 0:
        print("Positive")
    elif num<0:
        print("Negeative")
    else:
        print("Zero")
check_number(-3)


#4). 
def string_length(s):
    count = 0
    for char in s:
         count +=1
    return count 
print(string_length("python"))


#5).
def print_list(items):
    for i in items:
        print(i)
print_list([10,20,30])


#6). 
def cube(n):
    return n ** 3
print (cube(4))


#7).
def count_even(lst):
    count=0
    for i in lst:
        if i%2==0:
            count+=1
    return count
print(count_even([1,2,3,4,5]))


#8).
def greet(name):
    print("Hello", name + "!")

greet("Chatvika")


#9).
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1,2,3,4]))


#10).
def max_value(lst):
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum

print(max_value([3, 8, 1, 9, 2]))
