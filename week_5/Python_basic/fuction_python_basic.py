# 1
def is_even(n):
    return n%2==0
# 2
def factorial(n):
    result=1
    while n>0:
        result*=n
        n-=1
    return result
# 3
def digital_root(n):
    return
# 4
def is_palindrom(s):
    # return s==s[::-1]
    i=0
    length=len(s)-1
    while i<=length:
        if i==length:
            return True
        if s[i]==s[length]:
            i+=1
            length-=1
        else:
            return False
    return True

# 5
# Halper function
def sum_digits(n):
    sum_digit=0
    while n>0:
        sum_digit=sum_digit+n%10
        n//=10
    return sum_digit
# Main function
def one_digit(n):
    total_sum=0
    while n > 9:
        n=sum_digits(n)
    return n
print(one_digit(9875))
# 6
def count_digit(n):
    counter=0
    while n>0:
        counter+=1
        n//=10
    return counter
# 7
def reverse_num(n):
    is_negative = True
    if n<0:
        is_negative=False
        n=abs(n)
    reverse_digits=0
    while n>0:
        reverse_digits=(reverse_digits*10)+n%10
        n//=10
    return reverse_digits if is_negative else -1*reverse_digits
# 8
def zero_sorting(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.append(lst.pop(i))
    return lst
# 9
def lst_details(lst):
    sum_total=0
    min_num = lst[0]
    max_num = lst[0]
    for num in range(0,len(lst)):
        sum_total+=lst[num]
        if lst[num]>max_num:
            max_num=lst[num]
        if lst[num]<min_num:
            min_num=lst[num]
    print(f"The maximum num is: {max_num}")
    print(f"The minimum num is: {min_num}")
    print(f"The sum is: {sum_total}")
# 10
def reverse_lst(lst):
    # return lst[::-1]
    i=0
    length=len(lst)-1
    while i<=length:
        if i==len(lst):
            return lst
        lst[i],lst[length]=lst[length],lst[i]
        i+=1
        length-=1
    return lst
# 11
def unique_numbers(lst):
    new_lst=[]
    new_lst.append(lst[0])
    for i in range(1,len(lst)):
        if lst[i] in new_lst:
            continue
        new_lst.append(lst[i])
    return new_lst
print(unique_numbers([3,3,4,5,6,7,2,3,4,2,2,1,7,5]))
# print(is_even(8))
# print(factorial(7))
# print(is_palindrom("dsfjsad;fjb;fa"))
# print(count_digit(45623))
# print(reverse_num(-123456789))
# print(reverse_num(120000))
# print(reverse_lst([1,2,3,4,5,6,7,8,9,10]))
# print(lst_details([1,2,34,7,5]))