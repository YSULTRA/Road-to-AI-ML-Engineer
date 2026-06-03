print("Hello world!")


variableA = 5
variableB = 55/8
variableC = 5 + 4j

#Checking Types
print(type(variableA))
print(type(variableB))
print(type(variableC))


#Learning Strings
stringA = "my name is Yash Singh"
stringB = 'My name is Yash Singh'
stringC = """ Hello world
            my name is yash singh i am learning
            python for ai ml"""

print(type(stringA))
print(type(stringB))
print(type(stringC))

# All are same type just one is multi line way and no difference in "" and ''



#boolean
areYouHuman = True  #1
areYouRobot = False #0

print(type(areYouHuman))
print(type(areYouRobot))


character = "A"
print(ord(character)) # convert Ch to numeric code
print(chr(65)) # conver number code to CH


#Indexing
sampleString = "H$w Are You"
print(sampleString[1]) #positive indexing
print(sampleString[-10]) #negative indexing


#Slicing
print(sampleString[4:7:1])
print(sampleString[4::-2])

#Type Conversion

#Explicit Conversion
a = 0
print(bool(a)) # for 0 0.0 "" [] {} ()  convers is false rest True

a = "0"
print(bool(a))

b = "55.55"
b = float(b)
print(type(b))

#Implicit Conversion
print("Implicit Converisons")
a = 12
b = 12/5
print(type(b))
print(type(a))
print(type(8/9))