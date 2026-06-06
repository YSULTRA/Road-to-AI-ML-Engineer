def sum(a,b):
    print(f"The sum of two number is : {a+b}")

sum(5,5)


def greet(name , age):
    print(f"hello mr {name} and your age is {age}")

greet(age = 34,name = "Yash")


def defaultCheck(a,b=3):
    print(f"{a+b}")

defaultCheck(4)
defaultCheck(4,6)