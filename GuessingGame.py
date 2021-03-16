import random
randomNumber = random.randint(1,9)
chances = 0
while chances<5 :
    guess = int(input("enter your guess "))
    if guess == randomNumber:
        print("nice its correct")
        break
    elif guess < randomNumber :
        print("your guess was too low.", guess)
        
    else:
        print("your guess was too high.", guess)
    chances += 1
if not chances < 5 :
    print("you lost. The correct number is", randomNumber)