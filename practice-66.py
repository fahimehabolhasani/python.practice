import random

pc_number = random.randint(1 , 24)

i = 0
while True:
        
    user_number = int(input("enter your number :"))
    i = i + 1
    if user_number == pc_number:
        print("you won")
        print("game times :", i)
        break
    if user_number<pc_number:
        print("increase the number")
        
    if user_number>pc_number:
        print("reduce the number")