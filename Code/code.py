import time

student_name = input("Enter the Student's name to access their details on their points: ")

names = ["Adam", "Billy", "Colin"]
time.sleep(1)
if student_name in names:
    print("Welcome, {}.".format(student_name))
    time.sleep(0.5)
    print("Currently, you have:")
    time.sleep(1)
else:
    print("There is no such student in this school.")
    exit()

with open("Student_details/{}.txt".format(student_name), "r") as file:
    content = file.read()
    print(content)

lines = content.splitlines()
positives = int(lines[0].split()[0])
negatives = int(lines[1].split()[0])

time.sleep(1)
print("""

""")

print("Currently,in stock, there is")
time.sleep(1.2)
with open("Stock/Stock.txt", "r") as file:
    content_1 = file.read()
    print(content_1)

lines = content_1.splitlines()
pencils = int(lines[0].split()[0])
pens = int(lines[1].split()[0])
highlighters = int(lines[2].split()[0])
love_hearts_sweets = int(lines[3].split()[0])
haribos = int(lines[4].split()[0])
choclate = int(lines[5].split()[0])
spinners = int(lines[6].split()[0])
books = int(lines[7].split()[0])

item_1 = input(str("Enter the item that you would like to purchase :"))

if item_1 == "pencils":
    in_stock = pencils
    price = int(lines[0].split()[3])
    print(f"There are {pencils} {item_1} in stock")

elif item_1 == "pens":
    in_stock = pens
    price = int(lines[1].split()[3])
    print(f"There are {pens} {item_1} in stock")

elif item_1 == "highlighters":
    in_stock = highlighters
    price = int(lines[2].split()[3])
    print(f"There are {highlighters} {item_1} in stock")

elif item_1 == "love_heart_sweets":
    in_stock = love_hearts_sweets
    price = int(lines[3].split()[3])
    print(f"There are {love_hearts_sweets} {item_1} in stock")

elif item_1 == "haribos":
    in_stock = haribos
    price = int(lines[4].split()[3])
    print(f"There are {haribos} {item_1} in stock")

elif item_1 == "choclate":
    in_stock = choclate
    price = int(lines[5].split()[3])
    print(f"There are {choclate} {item_1} in stock")

elif item_1 == "spinners":
    in_stock = spinners
    price = int(lines[6].split()[3])
    print(f"There are {spinners} {item_1} in stock")

elif item_1 == "books":
    in_stock = books
    price = int(lines[7].split()[3])
    print(f"There are {books} {item_1} in stock")

else:
    print("Sorry, There is no such item in stock!")
    exit()

total = positives + negatives
quantity = int(input("How many {} would you like to get, currently you have a total of {} points.".format(item_1, total )))
if quantity > in_stock:
    print("Sorry, there is not enough stock for your order.")
    exit() 
else:
    print("You have ordered {} {}.".format(quantity, item_1))
    print("You have {} points.".format(total))
    print("The price of {} {} is {} points.".format(quantity, item_1, (price * quantity)))
    if total < (price * quantity):
        print("Sorry, you do not have enough points to make this purchase.")
        exit()
    else:
        print("You will have {} points left after this purchase.".format(total - (price * quantity)))
        assure = input("Are you sure you want to make this purchase? (yes/no) :")
        if assure == "yes":
            print("Thank you for your purchase, {}.".format(student_name))
            print("You have {} points left.".format(total - (price * quantity)))
            update_stock = in_stock - quantity
            with open("Stock/Stock.txt", "r") as file:
                lines = file.readlines()
            with open("Stock/Stock.txt", "w") as file:
                for line in lines:
                    if line.startswith(item_1):
                        file.write(f"{update_stock} {item_1} at {price} points\n")
                    else:
                        file.write(line)
        else:
            print("You have cancelled your purchase.")
            exit()
        