
#STRINGS
#string methods

name = "pythonjava"
print(name)
print(len(name))#length
print(name.lower()) #Converts string to lowercase.
print(name.upper())#converts string to upper
print(name.title())#First letter of each word becomes capital.
print(name.capitalize())#First letter of the string becomes capital.
print(name.strip())#Removes spaces from beginning & end.
print(name.replace("python","java"))#eplaces part of a string.
print(name.find("y"))#Returns index of the first match.
print(name.count("o"))#Counts how many times a character appears.
print(name.split())#Breaks string into a list.
#string properties
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())

#indexing

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(name[-1])
print(name[-2])
# print(name[-3])
print(name[-4])

#slicing
print(name[2:-1])

print(name[0:9:-1])
print(name[1:6:-1])

