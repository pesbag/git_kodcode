# 1
# for i in range(1,11):
#     if i%2==0:
#         continue
#     if i == 7:
#         break
#     print(i)
# 2
# while True:
#     password=input("Enter a password")
#     if password=="1234":
#         print("Welcome!")
#         break
# 3 A
# items_lst=[]
# while True:
#     product=input("Enter the next product")
#     if product == "done":
#         break
#     items_lst.append(product)
# print(items_lst if items_lst else [])
# 3 B
# for row in range (1,4):
#     for col in range(1,4):
#         if col==2:
#             break
#         print(f"({row},{col})")
# 4
# string=input("Enter a string").lower()
# vowels=["a","e","i","o","u"]
# counter=0
# for char in string:
#     if char in vowels:
#         counter+=1
# print(f"There is a {counter} vowels")
# 5
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i} x {j}={i*j}")

# 6
# reversed_string=""
# string=input("Enter a string")
# for n in range(len(string)-1,-1,-1):
#     reversed_string+=string[n]
# print(reversed_string)
# 7
# positive_number=int(input("Enter a positive number"))
# is_even=0
# while positive_number!=0:
#     if positive_number%2==0:
#         is_even+=1
#     positive_number//=10
# print(f"There is {is_even} even digits")
# 8
# double_str=""
# string=input("Enter a string")
# for i in range(0,len(string)):
#     double_str+=2*string[i]
# print(f"The double string is: {double_str}")
# 9
# max_num = 0
# while True:
#     number=int(input("Please enter a number"))
#     if number>max_num:
#         max_num=number
#     if number==0:
#         print(f"The highest enterd is {max_num}")
#         break
# 10
# string=input("Please enter a string")
# for char in string:
#     if not char.isdigit() and not char.isalpha():
#         print("False")
#         break
# print("True")
# 11
reverse_num=0
number=int(input("Please enter a nuber"))
while number !=0:
    reverse_num=(reverse_num*10)+number%10
    number//=10
print(f"The reverse number is {reverse_num}")