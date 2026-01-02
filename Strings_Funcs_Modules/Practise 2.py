# Write a function that returns the factorial of a number.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print (factorial(5))


# 2).Write a function that checks if a string contains only alphabets.
def is_only_alphabets(s):
    return s.isalpha()

print (is_only_alphabets("Hello"))
print(is_only_alphabets("Hello123"))
print(is_only_alphabets("Hello World"))

# 3). write a function that returns the sum of digits of a number.
def sum_of_digits(n):
    n=abs(n)
    total =0
    while n>0:
        total+=n%10
        n//10
        return total
print(sum_of_digits(123))
print(sum_of_digits(405))

# 4).   Write a function that removes all vowels from a string.
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result=""
    for ch in s:
        if ch not in vowels:
            result+=ch
    return result
print(remove_vowels("Hello World"))  
print(remove_vowels("Python"))

# 5).Write a function that counts uppercase and lowercase letters in a string.
def count_upper_lower(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower
# ex.
text = "Hello World"
u, l = count_upper_lower(text)
print("Uppercase:", u)
print("Lowercase:", l)

# 6).Write a function that checks if two strings are anagrams.

def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

# ex
print(are_anagrams("listen", "silent"))      
print(are_anagrams("Hello", "Olelh"))       
print(are_anagrams("apple", "pale"))        

# 7).Write a function that returns the unique elements from a list.
def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# ex

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
# Output: [1, 2, 3, 4, 5]

# 8).Write a function that returns a new list with squares of all numbers.
def square_list(lst):
    result = []
    for num in lst:
        result.append(num * num)
    return result
# ex
print(square_list([1, 2, 3, 4, 5]))

# 9). Write a function to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# ex
print(is_prime(7))  
print(is_prime(10)) 
# 10). Write a function that merges two dictionaries into one.
def merge_dicts(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d
# ex
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dicts(a, b))


# functions practise

# 1).Function to add two numbers
def add(a,b):
    return(a+b)
print(add(3,4))

# 2).Function to check even or odd
def even_odd(n):
    if n%2==0:
       return "Even"
    else:
       return "Odd"
print(even_odd(2))

# 3).Function to find factorial
def factorial(n):
    fact=1
    for i in range(1  ,n+1):
     fact=fact*i
    return fact
print(factorial(5))

# 4).Function to count vowels in a string
def count_vowels(s):
    count=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
    return count
print(count_vowels("chatvika"))

# 5).Function to count consonants
def count_consonents(s):
    count=0
    for ch in s:
        if ch not in "aeiouAEIOU" and s.isalpha():
            count+=1
    print(count)
count_consonents("Chatvika")

# 6).Function to check prime number
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "Prime"
    else:
        return"Not in prime"
print(is_prime(12))
# 7).Function to reverse a string
def function(n):
    return n[::-1]
print(function("he hello"))

# 8).Function to find largest number in a list
def largest_num(s):
    return max(s)
print(largest_num([1,2,3,4,5]))

# 9.Function to find square of each element in list
def square(n):
  return [i*i for i in n]
print(square([1,2,3]))

# 10).Check divisible by 5
def divisible_by_5(n):
    return n%5==0
print(divisible_by_5(500))

# 11.) Square and cube of a number
def square_cube(n):
    return n*n , n*n*n
print(square_cube(3))

# 12.Sum of even numbers up to n
def sum_even(n):
    total=0
    for i in range(1,n+1):     
        total+=i
    return total
print(sum_even(8))
# 13.)Write a function that counts how many words are present in a given string.
def function_count(s):
    count = 0
    for   ch in s.split():
        count += 1
    return count

print(function_count("Python is easy"))

# 14).Swap two numbers (without 3rd variable)
def swap(a,b):
    a,b=b,a
    return a,b
print(swap(20,50)) 




