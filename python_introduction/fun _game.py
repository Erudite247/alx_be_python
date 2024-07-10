import random 

secret_number = random.randint(1,10)
print("I'm thinking of a number between 1 and 10. Can you guess it?")
guess = None
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("That's not a valid number. Please enter a number between 1 and 10.")
       
    attempts = attempts + 1

    match guess:
        case _ if guess < secret_number:
            print("Nope, guess is a little bit low. Give it another shot!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")

        case _ if guess == secret_number:
            print (f"Congratulation! , you got it right. It took you {attempts} attempts to get it right")
