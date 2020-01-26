# Problem 3: Largest Prime Factor
# The prime factors or 13195 are 5, 7, 13, and 29. What is the largest prime factor of the number 600851475143?
import math 

# getting factors of a number
def getFactors(number):
    factors = []
    for potentialFactor in range(1, int(math.sqrt(number)) + 1):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number // potentialFactor) #need to append the potential factor as well as it's partner
    return factors

#determine if a number is prime
def isPrime(number):
    return len(getFactors(number)) == 2

allFactors = getFactors(600851475143)

#find highest number
largestPrimeFactor = 0
for factor in allFactors:
    if isPrime(factor) and factor > largestPrimeFactor:
        largestPrimeFactor = factor
print(largestPrimeFactor)