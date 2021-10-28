import random
a = int(input("Enter the lowest number"))
b = int(input("Enter the highest number"))
Num = random.randint(a,b)
print("I a guessing a number between",a ,"and",b)
playing = True
while playing:
    guess = int(input())
    if guess > Num:
        print("High! Try lower")
    if guess < Num:
        print ("Lower! Try Higher")
    if guess == Num:
        print("YOU WON!! YAY!!")