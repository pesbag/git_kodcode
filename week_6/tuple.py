from math import sqrt
# 1
def sum_of_tuple(tuple):
    sum_all=0
    for i in tuple:
        sum_all+=i
    return sum_all
# 2
def max_elemnt(tuple):
    max_num=tuple[0]
    for i in tuple:
        if i>max_num:
            max_num=i
    return max_num
# 3
def count_occur(tuple,num):
    counter=0
    for number in tuple:
        if number==num:
            counter+=1
    return counter
# 4
def reverse_tuple(tpl):
    new_lst=[]
    for num in range(len(tpl)-1,-1,-1):
        new_lst.append(tpl[num])
    return tuple(new_lst)

# def revers_tuple2(tple):
#     new_tuple=(tple[len(tple)-1],)
#     for num in range(len(tple)-1,-1,-1):
#         new_tuple+=(tple[num],)
# print("aaa",revers_tuple2((1,2,3,4,5)))
# 5
def swap_pairs(tpl):
    new_lst=[]
    for i in range(0,len(tpl)-1,2):
        new_lst.append(tpl[i+1])
        new_lst.append(tpl[i])
    return tuple(new_lst)
print(swap_pairs((1,2,3,4,5,6)))
# 6
def min_max(tpl):
    min_num=tpl[0]
    for num in tpl:
        if num < min_num:
            min_num=num
    return min_num, max_elemnt(tpl)
# 7
def distance_pointers(tpl1,tpl2):
    return sqrt((abs(tpl1[0]-tpl2[0]))**2+(abs(tpl1[1]-tpl2[1]))**2)
# 8
def merge_sort(tpl1,tpl2):
    new_tple=tpl1+tpl2
    return tuple(sorted(new_tple))
print(merge_sort((3,1,4),(1,5,9)))
# 9
def count_table(tpl):
    new_dict={}
    for char in range(0,len(tpl)):
        new_dict[tpl[char]]=new_dict.get(tpl[char],0)+1
    return tuple(new_dict.items())
print(count_table(('a','a','b','c','d','b','a','f')))
# 10
def rotate_tple(tpl,k):
    new_lst= tpl[len(tpl)-k:]+tpl[:len(tpl)-k]
    return tuple(new_lst)
print(rotate_tple((1,2,3,4,5),2))