"""
Python code to do sometihng that we can easily break

Most of it will be classic Algorithms.

This time around we are looking a the fibbonachi sequence
https://en.wikipedia.org/wiki/Fibonacci_number

Classic Recursive sequence where we have

  F0 = 0
  F1 = 1
  Fn = Fn-1 + Fn-2

In plain English

Given an Input of n

   - Return 0 if n is 0
   - Return 1 if n is 1
   - Return the sum of the Sequnce for N-1 and N-2
"""

import logging
import math


def fib(n):
    """
    Calculate the fibbonachi number for a given N
    """

    print(f"Calculating Fibbonchi for {n}")
    
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else
        value = fib(n-1) + fib(n-2)
    

def linearFib(n):
    """
    Did you know we can also make some Recursive functions linear.
    Google Diagonal Matrix for Recursive Functions and be amazed.
    """

    value = (1/math.sqrt(5)) * (math.pow(((1+math.sqrt(5))/2), n) - math.pow(((1 - math.sqrt(5))/2), n))
    return int(value) #floating point approximations
    
if __name__ == "__main__":
    out = fib(1)
    print(f"Fibbonachi of 1 is {out}")

    out = fib(10)
    print(f"Fibbonachi of 10 is {out}")

    out = linearFib(10)
    print(f"Linear Fibbonachi of 10 is {out}")
