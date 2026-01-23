#Scripts to compute the Bernoulli numbers, the switch indicates whether to output to file
#We are computing the so called topologist's Bernoulli numbers as defined in say Milnor-Stasheff (Appendix B)

from fractions import Fraction
#Fraction(value).denominator to get the denominator of a rational number
from sympy import sieve, prime, bernoulli
#all primes less than 19, [i for i in sieve.primerange(19)]
import math


def bernoulli_numbers_total(n, switch):
    #For the non-denominator parts we use sympy's built in bernoulli number function, and translate it to the topologists indexing
    bernoulli_nums = []
    for i in range(1,n+1):
        bernoulli_nums.append((-1)**(i+1)*bernoulli(2*i))

    #Output to file if switch is on
    if switch:
        with open("output.txt", "w") as f:
            f.write(str(bernoulli_nums))
    return bernoulli_nums

def bernoulli_numbers_denominator(n, switch):
    #This algorithm is suggested by Milnor-Stasheff Appendix B
    #These are easier to compute and do not grow as fast as the numerators
    bernoulli_nums = []
    primes = [i for i in sieve.primerange(2*n)]

    for k in range(1, n+1):
        prime_factors = []
        for p in primes:
            if  (2*k)%(p-1) == 0:
                i=0
                while (k % (p**i) == 0):
                    i += 1
                prime_factors.append(p**i)
        bernoulli_nums.append(math.prod(prime_factors)//math.gcd(k, math.prod(prime_factors)))

    
    
    #Output to file if switch is on
    if switch:
        with open("output.txt", "w") as f:
            f.write(str(bernoulli_nums))
    return bernoulli_nums

def bernoulli_numbers_numerator(n, switch):
    #We use the previous two functions to compute the numerators
    bernoulli_nums = []
    denoms = bernoulli_numbers_denominator(n, False)
    nums = bernoulli_numbers_total(n, False)

    for i in range(len(nums)):
        bernoulli_nums.append(nums[i]*denoms[i])

    #Output to file if switch is on
    if switch:
        with open("output.txt", "w") as f:
            f.write(str(bernoulli_nums))
    return bernoulli_nums

