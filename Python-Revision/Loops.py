
a = range(1,21,1)

# for i in a:
#     print(i)

# for i in range(21):
#     print(i)


# for i in range(21,-1,-3):
#     print(i)

# for i in range(5,(5*10)+1,5):
#     print(i)


for i in range(21):
    if i == 55:
        print("Break Called")
        break
    
    print(i)

else:
    print("Break is not called")




#Random Game

import random

noOfTries = 3
randomNumber = random.randint(1,10)
print(randomNumber)
while noOfTries > 0:

    guess = int(input("Enter the random number between 1 - 10: "))

    noOfTries -= 1

    if guess == randomNumber:
        print("Correct Answer")
        break
    elif guess < randomNumber:
        print("guess little bit higer")
    elif guess > randomNumber:
        print("Guess little bit lower")
    else:
        continue

else:
    print("You loose the Game") 
