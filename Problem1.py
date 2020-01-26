# Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def multiples():
    
    total_sum = 0
    #For all numbers below num
    for x in range(1,1000):
        if (x % 3 == 0 or x % 5 == 0):
            #print(x)
            total_sum += x
            x += 1
    
    return(total_sum)

num = str(1000)
print(multiples())