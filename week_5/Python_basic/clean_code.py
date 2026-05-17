# 1
def find_active_people(people_data):
    name_of_active_people = []
    for people in people_data:
        if people[1] >= 18 and people[2] == "True":
            name_of_active_people.append(people[0])
    return name_of_active_people

people_data_lst = [
    ["Dan", 25, "True"],
    ["Noa", 16, "True"],
    ["Yael", 30, "False"],
]

print(find_active_people(people_data_lst))

# 2
def check_validation(user_email, quantity, stock):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None
    return None
def check_for_price(quantity, product_price):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price
def update_quantity(stock, quantity):
    stock-=quantity
    return stock
def get_purchase_details(user_email, product_name,quantity,total_price):
    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = total_price
    order_status = "confirmed"
    return order_user, order_product, order_quantity, order_total, order_status
def print_info(order_information):
    print(f"Order {order_information[0]}: {order_information[1]} bought {order_information[2]}x {3} for ${order_information[4]}")

def handle_purchase(user_email, product_name, product_price, stock, quantity):
    check_validation(user_email, quantity, stock)
    total_price=check_for_price(quantity,product_price)

    num_of_items=update_quantity(stock,quantity)
    get_info=get_purchase_details(user_email, product_name, quantity, total_price)
    print_info(get_info)
    return None
# 3
def check_validation_name(new_name, new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True
def add_student(new_grade,grades):
    grades.append(new_grade)
def calculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for grade in grades if grade >= 90)
    failing_count = sum(1 for grade in grades if grade < 56)
    return average, top_count,failing_count
def print_data(names, grades, data_stats):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {data_stats[0]:.1f}")
    print(f"Top students: {data_stats[1]}")
    print(f"Failing: {data_stats[2]}")
def save_to_file(names,grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")
def manage_students(names, grades, new_name, new_grade):
    # validation
    is_valid=check_validation_name(new_name,new_grade)

    # add student
    add_student(new_grade, grades)

    # calculate stats
    stats=calculate_stats(grades)

    # print report
    print_data(names, grades, stats)

    # save to file
    save_to_file(names, grades)

    return names, grades

# 4
def check_validation_user(name, email):
    if not name or len(name) < 2:
        raise ValueError("Invalid name")
    if "@" not in email:
        raise ValueError("Invalid email")

def create_new_user(name,email):
    try:
        check_validation_user(name,email)
        return name, email, "user", "2024-01-01", True
    except ValueError:
        return None

# 5
def get_status(score):
    if score >= 90:
        status = "excellent"
    elif score >= 70:
        status = "good"
    elif score >= 55:
        status = "average"
    elif score < 55:
        status = "fail"
    else:
        status = "unknown"
    return status


def is_valid_age(age):
    if isinstance(age, int) and 0 < age < 120:
        return True
    return False

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"
# 6

def validate_student(name, grades):
    if not name:
        raise ValueError("missing name")
    if not grades:
        raise ValueError(f"{name} has no grades")

PASS_GRADE = 56
def calculate_student_stats(name, grades):
    average = sum(grades) / len(grades)
    return {
        "name": name,
        "average": round(average, 1),
        "status": "pass" if average >= PASS_GRADE else "fail",
        "highest": max(grades),
        "lowest": min(grades)
            }

def print_report(result_names, result_averages, result_statuses, result_lows, result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()
    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")

def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []

    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]

        try:
            validate_student(name, grades)
            stats = calculate_student_stats(name,grades)

            result_names.append(stats["name"])
            result_averages.append(stats["average"])
            result_statuses.append(stats["status"])
            result_highs.append(stats["highest"])
            result_lows.append(stats["lowest"])
        except ValueError as e:
            print(f"Error: {e}")
            continue

    print_report(result_names, result_averages, result_statuses, result_lows, result_highs)
    return result_names, result_averages, result_statuses



# 7
TAX = 0.17
PREMIUM_DISCOUNT = 0.9
VIP_DISCOUNT = 0.8
FREE_SHIPPING = 500
CHEAP_SHIPPING = 200
def process_cart(prices,quantities,user_type):
  total_price=0
  for i in range(len(prices)):
    price_for_product=prices[i]
    quantity_for_product=quantities[i]
    total_price=total_price+price_for_product*quantity_for_product
  # add tax for price
  total_price = total_price + total_price * TAX
  if user_type=='premium':
    #   get discount because he is a premium service
    total_price=total_price*PREMIUM_DISCOUNT
  #   get discount because he is a vip service
  elif user_type=='vip':
      total_price = total_price * VIP_DISCOUNT
  #   free shiping due to very higher price order
  if total_price>FREE_SHIPPING:
    shipping=0
  elif total_price > CHEAP_SHIPPING:
    #   cheap shiping because of higher price order
    shipping = 25
  else:
    #   a regular price order
    shipping=50
  total_price=total_price+shipping
  return total_price
