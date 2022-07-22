import random
n=20
to_be_guessed = int(n * random.random()) +1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess >0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess< to_be_guessed:
            print("Number too small")
    else:
        print("sorry that you are giving up!")
        break
else:
    print("Congratulation. you made it!")
