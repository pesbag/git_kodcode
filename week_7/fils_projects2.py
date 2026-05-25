def create_grades_file(file_name):
    with open(file_name,"w",encoding="utf-8") as f:
        students = [
            ("Dan", [85, 90, 78]),
            ("MOMO", [92, 88, 95]),
            ("Yoni", [70, 65, 80]),
            ("Avi", [100, 95, 98]),
            ("Sara", [60, 72, 68]),
        ]
        for s in students:
           f.write(f"{s[0]}, {str(s[1]).strip("[]")}\n")
            # f.write(f"{s[0]}, {s[1][0]}, {s[1][1]}, {s[1][2]}\n" )
create_grades_file("grades.txt")

def calculate_averages(file_name):
    avg_dict={}
    with open(file_name,"r") as f:
        for data in f.readlines():
            grades=[g.strip() for g in data.split(",")]
            avg_dict[str(grades[0])]=sum(int(x) for x in grades[1:])/(len(grades)-1)
    return avg_dict
print(calculate_averages("grades.txt"))

def save_results(averages, output_file_name):
    sort_avg=dict(sorted(averages.items(), key=lambda item: item[1],reverse=True))
    sum_total=0
    with open(output_file_name,"w") as result_f:
        for i,(k,v) in enumerate(sort_avg.items(),start=1):
            result_f.write(f"{i}. {k}: {v}\n")

        result_f.write("=== Statistics ===\n")
        for grade in sort_avg.values():
            sum_total+=grade

        result_f.write(f"Class average:{sum_total/len(sort_avg)}")
        max_name, max_grade = max(sort_avg.items(), key=lambda grade: grade[1])
        result_f.write(f"Highest: {max_name} ({max_grade})\n")
        min_name,min_grade=min(sort_avg.items(),key=lambda item:item[1])
        result_f.write(f"Lowest: {min_name} ({min_grade})\n")
        counter=0

        for i in sort_avg.values():
            if i>=60:
                counter+=1
        result_f.write(f"Passing(>=60): {counter}/{len(sort_avg)}")
    return result_f
avg=calculate_averages("grades.txt")
save_results(avg,"result.txt")
