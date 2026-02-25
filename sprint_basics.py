# 1)
name = input("Enter your name: ")
target_level= input("Enter your target: ")
target_year= int(input("Enter year: "))

print(f" I am {name}, aiming from {target_level} in Japan by {target_year}")


# 2)
price= float(input("Enter price: "))
quantity= int(input("Enter quantity: "))
p_name=input("Enter p_name: ")

print(f"The total cost of {p_name} is {price * quantity} ")


# 3)
cities=["Tokyo","Kyoto","Osaka" ]
cities.append("Hiroshima")
print(cities[1])


# 4)
N3_score = int(input("Enter your score: "))
if(N3_score>=95):
    print("pass")
else:
    print("Study hard")


# 5)
prog_lang=input("Enter your favorite language")
if(prog_lang.lower()== "python"):
    print("Great for DSA")
else:
    print("Good choice!")


# 6)
numbers=[1,2,3,4,5]
for i in numbers:
    print(i*i)


# 7)
countdown=5
while countdown > -1:
    print(countdown)
    countdown-=1


# 8)
def greet_dev(name, language):
    return f"Hello {name}, welcome to {language} pragramming!"

a=greet_dev("Shreyash", "Python")
print(a)


# 9)
product={
    "id": 1,
    "name" : "Fan",
    "price": 350 
}
a=product["price"]
print(a)


# 10)
product={
    "id": 1,
    "name" : "Fan",
    "price": 350 
}
product["stock"]=50
product["price"]=450
print(product)


# 11)
prices = [100, 200, 300, 400]
discounted_list=[i*0.9 for i in prices]
print(discounted_list)


# 12)
try:
    num=int(input("enter number: "))
    # print(num)
except ValueError:
     print("Value error occured") 


# 13)
user_data=[
    {
        "name": "Shreyash",
        "email": "shreyash@gmail.com"
    },
    {
        "name": "Yash",
        "email": "yash@gamilcom"
    }
]
user2= user_data[1]
name=user2["name"]
print(name)


# 14)
alphabet="abcdefghij"
print(alphabet[:5], end="")
print(alphabet[-3:])

# 15)
values=[1, 2, 2, 3, 4, 4, 5]
new_values=set(values)
print(new_values)

    





