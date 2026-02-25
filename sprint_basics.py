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


#6)
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





