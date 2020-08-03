import random
num = random.randint(1,100)
x=int(input("guess a number from 1 to 100:"))
while x != num:
    print("you guessed wrong.")
    x=int(input("guess a number from 1 to 100:"))
    if x == num:
        print("you guessed right!")
      