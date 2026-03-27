from bernoulli_numbers_generator import *
from sympy import sieve, prime, bernoulli

def epsilon(k):
    return int((3 - (-1)**k)/2)

def mersene(k):
    return int(2**(2*k - 2) * (2**(2*k - 1) - 1))

def bP_4k(k):
    bern = (-1)**(k+1)*bernoulli(2*k)
    print(bern)
    bern = bern/(4*k)
    print(bern)
    num_bern = bern.p #Sympy number.Rational object .p get numerator
    print(bern.p)
    print(epsilon(k)*mersene(k)*num_bern)
    return epsilon(k)*mersene(k)*num_bern
    
bP_4k(12)