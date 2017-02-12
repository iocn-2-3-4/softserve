#!/usr/bin/python

import random

#attempts = int(input("Enter number of attempts: "))
#min = int(input("Enter a min number of range: "))
#max = int(input("Enter a max number of range: "))

def game(min,max):

    attempts = int(input("Enter number of attempts: "))
    min = int(input("Enter a min number of range: "))
    max = int(input("Enter a max number of range: "))

    secret_number = random.randint(min,max)

    for attempt in range(attempts):
        guess = int(input("Your attempt: "))

        if guess < secret_number:
            print("Higher...")
        elif guess > secret_number:
            print("Lower...")
        else:
            print " "
            print "Congratulations!", secret_number
            print "You guessed it in", attempts, "attempts"

            break

    if guess != secret_number:
        print " "
        print "Sorry you reached the maximum number of tries"
        print "The secret number was", secret_number

game(min,max)
