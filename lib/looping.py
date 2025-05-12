#!/usr/bin/env python3

"""Module for looping-related functions."""

def happy_new_year():
    """Prints a countdown from 10 to 1 and a New Year message."""
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square(numbers):
    """Returns a list of squares of the given numbers."""
    return [num ** 2 for num in numbers]

def square_integers(numbers):
    """Returns a list of squares of the given numbers."""
    return [num ** 2 for num in numbers]

def fizzbuzz():
    """Prints numbers from 1 to 100 with FizzBuzz rules:
    - Print 'Fizz' for multiples of 3.
    - Print 'Buzz' for multiples of 5.
    - Print 'FizzBuzz' for multiples of both 3 and 5.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
