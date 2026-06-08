import requests

response=requests.get("https://jsonplaceholder.typicode.com/users/1")
data=response.json()
print(f"Name: {data["name"]}\nEmail: {data["email"]}\nCity: {data["address"]["city"]}")

response1=requests.get("https://jsonplaceholder.typicode.com/posts")
posts=response1.json()
print(len(posts))

response2=requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
posts=response2.json()
for post in posts:
    print("The title is:")
    print(post["title"])