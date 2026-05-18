def sum_values(dict):
    sum_all=0
    for num in dict.values():
        sum_all+=num
    return sum_all
# print(sum_values( {"a": 1, "b": 2, "c": 3}))
# 2
def find_max_key(dict):
    return max(dict, key=dict.get)
# print(find_max_key({"a": 3, "b": 7, "c": 5}))
# 3
def count_char(str):
    chars_dict={}
    for char in str:
        chars_dict[char]=chars_dict.get(char,0)+1
    return chars_dict
# print(count_char("banana"))
# 4
def swap_dict(dict):
    new_dict={}
    for k,v in dict.items():
        new_dict[v]=k
    return new_dict
# print(swap_dict({"a": 1, "b": 2, "c": 3}))
# 5
def merge_dict(dict1,dict2):
    new_dict=dict1.copy()
    new_dict.update(dict2)
    return new_dict
# print(merge_dict( {"a": 1, "b": 2}, {"b": 20, "c": 30}))
# 6
def filterd_dict(dict,thrashold):
    new_dict={}
    for k, v in dict.items():
        if v<=thrashold:
            continue
        new_dict[k]=new_dict.get(k,v)
    return new_dict
# print(filterd_dict( {"a": 1, "b": 5, "c": 3, "d": 8},3))
# 7
def group_by_first_letter(lst):
    new_dict={}
    for word in lst:
        if word[0] not in new_dict:
            new_dict[word[0]]=[word]
        else:
            new_dict[word[0]].append(word)
    return new_dict
# print(group_by_first_letter(["apple", "ant", "banana", "berry", "cherry"]))
# 8
def separate_dict(str):
    new_dict={}
    words=[word.strip() for word in str.split()]
    for w in words:
        new_dict[w]=new_dict.get(w,0)+1
    return new_dict
# print(separate_dict( "the cat sat on the mat mat"))
# 9
def keys_in_both(dict1,dict2):
    new_lst=[]
    for k in dict1:
        if k not in dict2:
            continue
        new_lst.append(k)
    return new_lst
# print(keys_in_both({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7}))
# 10
def most_frequent_val(dict):
    new_dict={}
    for k in dict.values():
        new_dict[k]=new_dict.get(k,0)+1
    return max(new_dict, key=new_dict.get)
print(most_frequent_val( {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}))