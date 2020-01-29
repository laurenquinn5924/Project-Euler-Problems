# The sum of the squares of the first ten natural numbers is,

# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,
# 	(1+2+...+10)^2=55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
# 	3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# function to add 1 to 100 and square the result

def addNumbers1to100():
	sum = 0
	for i in range(1, 101):
		sum += i
	
	return sum**2

# print(addNumbers1to100())

# Add up sum of each squared number and return the sum
def squareNumberAndAddToSum():
	sum = 0
	for i in range(1, 101):
		sum += i**2

	return sum

# Subtract the results to find the square of the sum
def finalSquareOfTheSum():
	return addNumbers1to100() - squareNumberAndAddToSum()

print(finalSquareOfTheSum())
