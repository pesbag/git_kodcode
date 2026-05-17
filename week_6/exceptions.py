# 1
def safe_int(s):
    try: return int(s)
    except (ValueError, TypeError):
        return None
# 2
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "undefined"
print(safe_divide(5,3))
# 3
def get_value(d,key):
    try:
        return d[key]
    except KeyError:
        return "missing"
# 4
def parse_ints(values):
    new_lst=[]
    for item in values:
        try:
            new_int=int(item)
            new_lst.append(new_int)
        except ValueError:
            continue
    return new_lst
print(parse_ints(['1','34','fssa','5','6']))
# 5
def set_age(age):
    try:
        if 150>=age>0:
            return age
        else:
            raise ValueError
    except ValueError:
        raise ValueError("Error age is not valid")
# 6
def retry(func,n):
    for index in range(n):
        try:
            return func()
        except Exception:
            if index == n-1:
                raise
# 7
def error_count(funcs):
    counter=0
    for function in funcs:
        try:
            function()
        except Exception:
            counter+=1
    return counter
# 8
def load_config(path):
    try:
        with open(path,"r") as f:
            int(f.readline())
    except Exception as e:
        raise RuntimeError("failed to load config") from e

