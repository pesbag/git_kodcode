# 1
x = input("Enter an integer")
try:
    y=int(x)
except ValueError:
    raise "Value error"
print(not bool(y%2))
# 2
x=int(input("Enter first variable"))
print(f"The first variable is: {x}")
y=int(input("Enter second variable"))
print(f"The second variable is: {y}")
y=x+y-y
x=y-x

y=y-x
print(f"the first varaible after swap is: {x}")
print(f"the second varaible after swap is: {y}")
# 3
num=int(input("Enter a 3 digits number"))
sum3=num%10+(num//10)%10+(num//100)%10
# 4
weight=float(input("Please enter your weight"))
height=float(input("Please enter your height"))
print(f"Your BMI is {weight/((height/100)**2):.2f}")
# 5
decimal_num=float(input("Please enter a decimal number"))
print(f"The integer part of the number is: {int(decimal_num)}")
print(f"The fraction part of the number is: {decimal_num-int(decimal_num)}")