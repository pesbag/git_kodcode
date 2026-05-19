def public_names(m):
    new_lst=[]
    results=dir(m)
    for func in results:
        if func[0]=='_':
            continue
        new_lst.append(func)
    return new_lst
print(public_names(("math")))