import math,random

print("The syntax for power 2**3:")
print(2**3)
print(math.pi)
print(random.random())
print(random.choice([1, 2, 34, 5, 6]))

print("This is normal operation and if you want only integers then")
print(7/2)

print("use extra slash")
print(7//2)

# numpy is close to matlab
# it also handles complex number
# set is also treated as number here
# boolean is also number mostly

# it is usually a good practice that data types of bothe the integers should be same

# usually this is the thing int(value) float(value)

# >>> x=3
# >>> y=4
# >>> z=5
# >>> x,y,z
# (3, 4, 5) this is the syntax here 
# cautious while calling api call {} its not dict here its tuple

# >>> x<y and y<z
# True

# trunc what is does is it gives the values closest to the zero(in number without decimal)
math.trunc(-2.8)

# lets look at imaginary number
x=(1+2j)
print(x*3)

#now lets beyound decimal
# >>> 0x20
# 32
# >>> 0xFF
# 255
# >>> 0b11
# 3
# >>> oct(64)
# '0o100'
# >>> hex(64)
# '0x40'
# >>> bin(64)
# '0b1000000'

# >>> int('72',16)
# 114

# bitwise operation
# >>> x=1
# >>> x << 2
# 4
# >>> x | 2
# 3

# random functions
# random.randomint()
# randome.shuffle(list)

# python doesnit works properly with decimal
# >>> 0.1+0.1+0.1-0.3
# 5.551115123125783e-17

# this is the better approach to handle decimals in python
# >>> from decimal import Decimal
# >>> Decimal('0.1') wrap your decimal like these
# Decimal('0.1')

# >>> from fractions import Fraction similar to decimal
# >>> myf = Fraction(2,7)
# >>> myf
# Fraction(2, 7)

# this is how we work with sets all the operations on sets are possible
# >>> setone ={1,2,3}
# >>> setone & {1} & for intersection
# {1}
# for empty set python returns () not curly braces
# >>> setone-{1,2,3}
# set() so the point to note here is if you want to denote empty set use paranthesis


# >>> type({}) because {} is fro dictionary
# <class 'dict'>

# object is diffrent but values are same
# >>> True == 1
# True
# >>> True is 1
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
# False