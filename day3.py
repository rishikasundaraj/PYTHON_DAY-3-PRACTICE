#Digit Sum using for
n=12345
sum=0
for i in str(n):
    sum+=int(i)
print(sum)

#Digit count using for
n=12345
count=0
for i in str(n):
    count+=1
print(count)

#Reverse a Number using for
n=989
original=n
reverse=0
for i in range (len(str(n))):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)

#Write a Python program to find the first number divisible by 7 between 1 and 50.
for i in range(1,51):
    if i%7==0:
        break
print(i)

#Write a Python program to print all numbers from 1 to 20 except the numbers divisible by 3.
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

#Nested for loop
#Print this pattern:*
n="*"
for i in range (5,0,-1):
    for j in range (i):
        print(n,end=" ")
    print()


#Nested for loop
#Print this pattern:*
n="*"
for i in range (1,6):
    for j in range (i):
        print(n,end=" ")
    print()

#Print this pattern:
#1
#12
#123
#1234
#12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Problem 1: Find the largest number among 5 numbers
n=(10,25,7,42,18)
largest=0
for i in n:
    if i>largest:
        largest=i
print("Largest number is:",largest)

#Problem 2 — Count Positive Numbers
n=[10,-3,7,0,-8]
count=0
for i in n:
    if i>=0:
        count+=1
print("positive number",count)

#Next Problem — Find the Smallest Number
n=[12,5,8,9,10]
smallest=n[0]
for i in n:
    if i<smallest:
        smallest=i
print("smallest",smallest)

#Count Even and Odd Numbers
n=[12, 5, 8, 3, 19, 20, 7]
count_even=0
count_odd=0
for i in n:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(count_even)
print(count_odd)

#Next Problem — Find the Largest Even Number
n = [12, 5, 8, 3, 19, 20, 7, 14]
largest=n[0]
for i in n:
    if i%2==0 and i> largest:
        largest=i
        print(largest)

#Next Problem — Remove Duplicate Numbers
n = [2, 4, 2, 6, 4, 8, 6]
unique=[]
for i in n:
    if i not in unique:
        unique.append(i)
        print(i)

#second largest 
n = [10, 25, 7, 42, 18]

largest = n[0]
second = n[0]

for i in n:
    if i > largest:
        second=largest
        largest=i
    elif i > second and i !=largest:
        second=i
print(second)

#Next Problem: Count Numbers Greater Than 10
n=[5, 12, 8, 25, 17, 3, 40]
greater_count=n[0]
for i in n:
    if n>10:
        greater_count+=1