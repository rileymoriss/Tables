#Scripts to compute the Bernoulli numbers, the switch indicates whether to output to file
#We are computing the so called topologist's Bernoulli numbers as defined in say Milnor-Stasheff (Appendix B)

from fractions import Fraction
#Fraction(value).denominator to get the denominator of a rational number
from sympy import sieve, prime
#all primes less than 19, [i for i in sieve.primerange(19)]
import math


def bernoulli_numbers_total(n, switch):
    return

def bernoulli_numbers_numerator(n, switch):
    return

def bernoulli_numbers_denominator(n, switch):
    #This algorithm is suggested by Milnor-Stasheff Appendix B
    bernoulli_nums = []
    primes = [i for i in sieve.primerange(2*n)]
    print("Inside the function, primes=", primes)

    for k in range(1, n+1):
        print("k=", k)
        prime_factors = []
        for p in primes:
            print("prime factors", prime_factors)
            if  (2*k)%(p-1) == 0:
                i=0
                while (k % (p**i) == 0):
                    i += 1
                    print("inside while p=", p, " i=", i)
                prime_factors.append(p**i)
                print("prime factors", prime_factors)

        print("prime_factors=", prime_factors)
        bernoulli_nums.append(math.prod(prime_factors)//math.gcd(k, math.prod(prime_factors)))
        print("product of primes: ",math.prod(prime_factors))
        print("dividing: ", k/(math.prod(prime_factors)))
        print("denominator: ", Fraction(k/(math.prod(prime_factors))).denominator)
        print("bernoulli_nums=", bernoulli_nums)
    
    
    #Output to file if switch is on
    if switch:
        with open("output.txt", "w") as f:
            for num in bernoulli_nums:
                f.write(str(num))
    return bernoulli_nums