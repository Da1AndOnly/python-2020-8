import random
a = 1
b = 100
num = random.randint(a,b)
while True:
    print("the number is inbetween%d-%d"%(a,b))
    ans = int(input('enter a number:'))
    if ans>b:
        break
    elif ans<a:
        break
    elif ans>num:
        b = ans
    elif ans<num:
        a = ans
    elif ans == num:
        print("you guessed the right number!")
    