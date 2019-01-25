# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumofthesquares(a):
    totalone=0
    for i in range(1,a+1):
        totalone+=pow(i,2)
    return totalone
sumofthesquares(10)
def thesquareofthesum(b):
    totaltwo=0
    sum_of_i=0
    for i in range(1,b+1):
        sum_of_i+=i
    totaltwo=pow(sum_of_i,2)
    return totaltwo


x=sumofthesquares(10)
y=thesquareofthesum(10)
print(y-x)
