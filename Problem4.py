# Problem 4: Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Step 1: Create is_palindrome function
# Change number to string to be able to compare characters
# Compare string to reversed string, if same return True

def isPalindrome(number):
    numAsAString = str(number)
    a = numAsAString[0:]
    b = numAsAString[::-1]
    if a == b:
        return True
    
# Step 2: Create function to multiply three digit numbers, range(100, 1000)

def makePalindrome():
    palindromes = []
    
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(i*j):
                #print(i, j)
                palindromes.append(i*j)
    palindromes.sort()
    return palindromes
print(makePalindrome())