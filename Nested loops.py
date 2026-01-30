# nested Loops

# 1).
for i in range(3):
    for j in range(1,11):
        print(j,end=" ")
    print()
    
# 2).
for i in range(5):
    for j in range(1,21):
        print(j ,end=" ")
    print()

# nested while loop:

# 1). 
multiplier=1
while multiplier<=3:
    item=1
    while item<=10:
     print(multiplier, "*",item ,"=",multiplier *item )
     item+=1
    multiplier+=1
    print("")

  
#  2). 
list1 =[1,2,3]
list2 =[4,5,6]
i = 0
j = 0
while i < len(list1):
    while j < len(list2):
        print(list1[i], list2[j])
        j += 1
    print()
    i += 1
  
# 3).Print numbers from 1 to 3, each printed 2 times
i=1
while i<=3:
    j=1
    while j<=2:
        print(i)
        j+=1
    i+=1

# 4).Print a 2 × 3 star pattern
i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print("*", end=" ")
        j += 1
    print()
    i += 1
# 5).Print
# 1 2
# 1 2
# 1 2
i=1
while i<=3:
    j=1
    while j<=2:
        print(j,end=" ")
        j+=1
    print()
    i+=1
        
# 6).Print characters of "PY" twice
s="PY"
i=1
while i <=2:
    j=0
    while j<len(s):
        print(s[j])
        j+=1
    i+=1
  
#  7).Pattern
# 12
# 123 
i=1
while i <=3:
    j=1
    while j <=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1