import pandas as pd
try:
    df=pd.read_csv("tracks.csv")
except FileNotFoundError:
    print("Error file not found")
head=df.head()
head3=df.head(3)
df.info()
df.describe()
df.shape
c_speed=df["speed"]
x=df[["id","speed"]]
avg=df["speed"].mean()
mx=df["speed"].max()
print(c_speed)
