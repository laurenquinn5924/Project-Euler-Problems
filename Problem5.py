def isDivisible1to20(number):
	for i in range(1, 21):
			if number % i != 0:
					return False
	return True


def smallestMultiple(number):
	while True:
		if isDivisible1to20(number):
				return number
		number += 1

print(smallestMultiple(1))
