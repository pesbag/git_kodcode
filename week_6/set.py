# 1
def remove_dup(lst):
    return list(set(lst))
# print(remove_dup([1, 2, 2, 3, 1, 4, 3]))
# 2
def count_unique_elements(lst):
    counter=0
    for _ in set(lst):
        counter+=1
    return counter
# print(count_unique_elements([1, 2, 2, 3, 1, 4]))
# 3
def common_element(lst1,lst2):
    new_lst=[]
    set1=set(lst1)
    set2=set(lst2)
    for i in set1:
        if i in set2:
            new_lst.append(i)
    return sorted(new_lst)
# print(common_element([1, 2, 3, 4], [3, 4, 5, 6]))
# 4
def appear_in_one(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return sorted(set1^set2)
# print(appear_in_one( [1, 2, 3, 4], [3, 4, 5, 6]))
# 5
def is_subset(lst1,lst2):
    return set(lst1).issubset(set(set(lst2)))
# print(is_subset( [1, 2, 3], [1, 2, 3, 4, 5]))
# 6
def unique_chars(str):
    return len(str)==len(set(str))
# print(unique_chars("hello"))
# 7
def first_reapeted(lst):
    new_set=set()
    for num in lst:
        if num in new_set:
            return num
        new_set.add(num)
    return None
# print(first_reapeted( [1, 2, 3]))
# 8
def distinct_words(str):
    words=[w.strip().lower() for w in str.split()]
    return len(set(words))
# print(distinct_words("The cat and the dog and the bird"))
# 9
def pair_sum_exists(lst,num):
    new_set=set()
    for i in range(0,len(lst)):
        diff=num-lst[i]
        if diff in new_set:
            return True
        new_set.add(lst[i])
    return False
# print(pair_sum_exists( [3, 1,4 , 7, 2],6))
def pair_distinct_sum_exists(lst,num):
    new_set=set()
    for i in range(0,len(lst)):
        diff=num-lst[i]
        if diff in new_set and diff!=lst[i]:
            return True
        new_set.add(lst[i])
    return False
# print(pair_distinct_sum_exists( [3, 1,4 , 7, 2],6))
# 10
def symnetric_diff(lst1,lst2):
    new_lst = []
    set1 = set(lst1)
    set2 = set(lst2)
    for i in set1:
        if i not in set2:
            new_lst.append(i)
    for j in set2:
        if j not in set1:
            new_lst.append(j)
    return sorted(new_lst)
# print(symnetric_diff([1, 2, 3, 4], [3, 4, 5, 6]))
