## ex6.1

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
# x = 1
# y = x + 1
# print(c(x, y+3, x+y))

# ex6.2
# The Ackermann function

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


#print(ackermann(3, 4))

# ex6.3
#  A palindrome is a word that is spelled the same backward and forward, like "noon" and "redivider"
#  Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise.

def is_palindrome(text):
	if len(text)<2:
		return True
	return is_palindrome(text[1:-1]) if text[0] == text[-1] else False

# print(is_palindrome("allen"))

# ex6.4 
# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b and returns True if a is a power of b.

def is_power(a,b):
	''' Return  the true if a is a power of b otherwise the false
	a, b  : non-negative integers
	0 is a power only of zero
	1 is a power of any number : x**0 = 1
	'''
	if a == 1:
		return True
	return a%b==0 and is_power(a/b,b)

# print(is_power(1,0))

# ex6.5
# The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
# As a base case, we can use gcd(a,0) = a
# Write a function called gcd that takes parameters a and b and returns their greatest common divisor.

def gcd(a,b):
	'''return the greatest common divisor of a and b '''
	if a == 0:
		return b
	if b == 0:
		return a
	if a == 1 or b ==1:
		return 1
	mod = a%b if a>b else b%a
	b = b if a >b else a
	print(mod,b)
	return gcd(mod,b)

import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
print(gcd(1212121212121,3432424255235))
