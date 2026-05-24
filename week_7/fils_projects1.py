import os
def create_file():
    with open("diary.txt","a", encoding="utf-8") as f:
        f.write("12-01-2015: sunday do homework\n")
        f.write("13-01-2015: monday go to work\n")
        f.write("14-01-2015: thursday vacation\n")
    print("The file was created succesfully!")
    with open("diary.txt","r") as f:
        print(f.read())

def add_new_entry(file_name,date, content):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"{date}: {content}\n")

def search_diary(file_name,keyword):
    with open(file_name,"r",encoding="utf-8") as f:
        new_lst=[]
        lines=f.readlines()
        for line in lines:
            words_in_line=line.strip().split()
            if keyword in words_in_line:
                new_lst.append(line)
        return new_lst
def safe_read_diary(file_name):
    if not os.path.exists(file_name):
        print(f"Error the file {file_name} is not exist")
    else:
        with open(file_name,"r", encoding="utf-8") as f:
            print(f.read())
print(search_diary("diary.txt","thursday"))
create_file()
add_new_entry("diary.txt", "03-08-2019", "hello from the future ")
