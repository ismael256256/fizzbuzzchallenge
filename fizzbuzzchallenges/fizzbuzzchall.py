
from fizz import fizz
from buzz import buzz
from fizzbuzz import fizzbuzz

def fizzbuzzchall(n):
    if fizzbuzz(n):
        fizzbuzz(n)
    elif fizz(n):
            fizz(n)
    elif buzz(n):
            buzz(n)
        

fizzbuzzchall(4)