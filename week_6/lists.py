#
def calc_sum(lst):
    total_sum=0
    for elemnt in lst:
        total_sum+=elemnt
    return total_sum
# 2
def find_max(lst):
    max_num=lst[0]
    for number in range(1,len(lst)):
        if lst[number]>max_num:
            max_num=lst[number]
    return max_num
# 3
def count_occurrence(lst,num):
    counter=0
    for number in lst:
        if number==num:
            counter+=1
    return counter
# 4
def reverse_lst(lst):
    rev_lst=[]
    for number in range(len(lst)-1,-1,-1):
        rev_lst.append(lst[number])
    return rev_lst
# print(reverse_lst([1,2,3,4,5,67]))
# 5
def remove_duplicate(lst):
    unique_lst=[lst[0]]
    for i in range(1,len(lst)):
        if lst[i] not in unique_lst:
            unique_lst.append(lst[i])
    return unique_lst
# print(remove_duplicate([1,11,1,3,4,4,56,6,6,6,67,77,1,11,8]))
# 6
def second_largest(lst):
    if len(lst)<=1:
        return None
    first_max=lst[0]
    second_max=None
    for i in range(1,len(lst)):
        if lst[i]>first_max:
            second_max=first_max
            first_max=lst[i]
        elif first_max>lst[i] and (second_max is None or lst[i] > second_max):
            second_max=lst[i]
    return second_max
print(second_largest([10,8,5]))
# 7
def merge_lst(lst1,lst2):
    new_sorted_lst=[]
    j,i=0,0
    while i < len(lst1) and j<len(lst2):
        if lst1[i]<=lst2[j]:
            new_sorted_lst.append(lst1[i])
            i+=1
        else:
            new_sorted_lst.append(lst2[j])
            j+=1
    if len(lst1)==i:
        new_sorted_lst.extend(lst2[j:])
    else:
        new_sorted_lst.extend(lst1[i:])
    return new_sorted_lst
print(merge_lst([1,3,5,5,7,9,11,13],[2,3,4,6,8]))
# 8
def rotate_lst(lst,k):
    k=k % len(lst)
    return lst[len(lst)-k:] + lst[:len(lst)-k]
# print(rotate_lst([1,2,3,4,5],2))
