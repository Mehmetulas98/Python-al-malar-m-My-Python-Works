# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math
#ı used this function for is number prime?it gives True or false
def isitprime(n):
    if n <= 1:          # negative numbers, 0 or 1
        return False
    if n <= 3:          # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
number=1
#counter for "st prime number"
counter=0
while counter!=10001:
    isitprime(number)
    if isitprime(number)==True:
        counter+=1
        print(number,"is prime and it is",counter,"st prime number")
    number+=1