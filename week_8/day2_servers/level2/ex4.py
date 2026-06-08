import requests

post_result=requests.get("https://jsonplaceholder.typicode.com/posts")
post_data=post_result.json()
print(post_data)
users_result=requests.get("https://jsonplaceholder.typicode.com/users")
users_data=users_result.json()
print(users_data)
new_dict1=[]
for p in users_data:
    new_dict1.append({"id":p["id"],"auther":p["name"]})
# for p in post_data:
#     new_dict2.append({"id":p["id"], "title":p["title"]})
for dic in post_data:
    # new_dict_final.append()
    print(f'{dic['title']},{new_dict1[dic['userId']-1]['auther']}')
    # d = requests.post(f"https://jsonplaceholder.typicode.com/posts?id={p["id"]}",json=new_dict)
    # print(d.status_code)

