# 16)
with open("goal.txt", "w+") as f:
    f.write("Learning python for Japan 2026")
    f.seek(0)
    print("Content of the file is : ", f.read())


# 17)
with open("goal.txt", "a")as f:
    f.write("\nAnd i will master Katagana this week!")

with open("goal.txt","r")as f:
    print(f.read())


# 18)
multiply= lambda a,b :a*b
print(multiply(5,6))


# 19)
price=[10, 20, 30, 40]
yen = list(map(lambda x: x*150, price))
print(yen)


# 20)
prices= [5, 120, 45, 200, 15, 90]
new_list=list(filter(lambda x : x >100, prices))
print(new_list)


# 21)
class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

s1=Product("Laptop", 150000)
print(f"Product: {s1.name} \nPrice {s1.price} yen")


# 22)
class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def apply_discount(self, percent):
        self.price= self.price *(1-percent/100)
        print(f"Discount applied! New Price is : {self.price}")

s1=Product("Laptop", 150000)
s1.apply_discount(10)


# 23)
class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class Electronic(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty=warranty

phone=Electronic("Samsung", 120000, 24)
print(f"Your phone is {phone.name}. The price of the phone is {phone.price} with a warranty of {phone.warranty} months")


# 24)
try:
    number=int(input("Enter your number: "))
    num=100/number
    print(f"Output is: {num}")
except ZeroDivisionError:
    print("Error: You can not divide by Zero!")
except ValueError:
    print("Error: Please enter valid number, no text")


# 25)
import math 
import random

root=math.sqrt(144)
power=math.pow(2, 8)

random_number=random.randint(1, 100)

print(f"Square root of 144 is: {root}")
print(f"2 to the power 8 is: {power}")
print(f"Random number between 1 and 100 is : {random_number}")


# 26)
number= [1, 2, 3, 4, 5]
new_list=[x*x for x in number if x>2]
print(new_list)


# 27)
import os
cwd=os.getcwd()
print(f"Currently I am in: {cwd}")

files=os.listdir(".")
print(f"Files in this folder: {files}")


# 28)
import json
data= {
    "name": "Shreyash",
    "gmail": "shreyash@gmail.com"
}
string_json=json.dumps(data)
print(string_json)
print(type(string_json))


# 29)
import json
json_data= '{"user": "Shreyash", "status": "Coding", "level": 29}'

user_dict=json.loads(json_data)
print(f"User Name: {user_dict['user']}")
print(type(user_dict))


# 30)
import json
class Order:
    def __init__(self, item_name, price):
        self.item_name=item_name
        self.price=price
    def to_dict(self):
        return{"items": self.item_name, "price": self.price}
    
my_order=Order("Mechanical Keyboard", 8000)
order_data=my_order.to_dict()

try:
    with open("order.json", "w")as f:
        json.dump(order_data, f)
    print("Order successfully saved to order.json!")
except Exception as e:
    print(f"An error occurred: {e}")
