#!/usr/bin/python

import random

def game(min, max):

    min = int(input("Enter a min number of range: "))
    max = int(input("Enter a max number of range: "))

    secret_number = random.randint(min,max)

    attempt = int(input('Your attempt: '))

    if attempt != secret_number:
        print("Try again!")
    elif attempt == secret_number:
        print("Congratulations!")

game(min, max)
