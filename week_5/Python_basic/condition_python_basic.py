#1
from curses.ascii import isspace

age = int(input("Enter your age"))
if 120 <= age <= 0:
    print("Invalid")
elif 12 >= age > 0:
    print("Child")
elif 17 >= age >= 13:
    print("Teen")
else:
    print("Adult")
#2
character=int(input("Please enter a character"))
if character<65 or 90<character<97 or character>122:
    print("Invalid")
if character in ["a","e","i","o","u"]:
    print("Vowel")
else:
    print("Consonant")
#3
age= int(input("Enter your age"))
VIP= input("Enter vip exist")
if age <= 16:
    print("Reject")
if (age >=18 and VIP=="yes") or age in [19,20,21]:
    print("Enter")
else:
    print("Sorry you can not enter")
#4
password=int(input("Enter a password"))
saved_password="12345678"
if password==saved_password:
    print("Access granted")
elif len(str(password))<8:
    print("Too short")
else:
    print("Wrong password")
#5
x_coordinate = int(input("Enter x coordinate"))
y_coordinate = int(input("Enter y coordinate"))
if 10<x_coordinate<50 and 20<y_coordinate<80:
    print("Inside the rectangle")
if (x_coordinate==10 or x_coordinate==50) and (y_coordinate==20 or y_coordinate == 80):
    print("On the edge")
else:
    print("Outside the rectangle")
#6
name=str(input("Please enter your name"))
name=name.isspace() or "Anonymous"
print(name)
#8
a=int(input("Enter firs number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
positive=(a>0)+(b>0)+(c>0)
print(f"There is a {positive} numbers")
#10
score = int(input("Enter a score"))
result = "A" if 100>=score>=90 else "B" if 90>score>=80 else "C" if 80>score>=70 else "F"
# result= (100>=score>=90 and "A") or (90>score>=80 and "B") or (80>score>=70 and "C") or (70>score and "F")
print(result)
