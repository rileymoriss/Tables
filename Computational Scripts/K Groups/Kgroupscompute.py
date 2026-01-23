#According to Weibel the other than zero mod 4 the K groups have been computed
#We couldnt find this computation, however it seems that it probably follows from some computations in number theory
#Taking his statements as true, we are writing this script to just list out the groups that he has claimed.
#The are finitely generated abelian groups, so we can list them as direct sums of cyclic groups, the numbers that we list therefore corespong to the cyclic summands. 
#Note that we will systematically ignore the free abelian parts, as they are not of interest for our purposes and can be written down explicitly (they are known)
#We will assume Van Divers conjecture, so a zero in the list is conjectural in degree 4k and in degree 5 mod 8 is because there is no torsion.
#The K groups have only a single summand and so we will have just a list of integers.

from sympy import sieve, prime, bernoulli, Rational, S, pi
from pathlib import Path
import sys

# Add path to import from Bernoulli Numbers module
sys.path.append(str(Path(__file__).parent.parent / "Bernoulli Numbers"))
from bernoulli_numbers_generator import *

#How many groups to compute
n = 24

#Need both numerator and denominator of Bernoulli numbers so compute the full number in advance
bernoulli_nums = bernoulli_numbers_total(n, False)
intermerdates = [bernoulli_nums[i]/(4*(i+1)) for i in range(n)]
numerators = [intermerdates[i].numerator for i in range(n)]
denominators = [intermerdates[i].denominator for i in range(n)]

#Initialize list
K_groups = []

for i in range(n):
    if i%4 == 0:
        #Conjectural
        K_groups.append(1)
    elif i%8 == 5:
        K_groups.append(1)
    elif i%8 == 1:
        K_groups.append(2)
    elif i%8 == 2:
        #Conjectural for all n but known for low n.
        K_groups.append(2*numerators[((i+2) // 4)-1])
    elif i%8 == 6:
        #Conjectural for all n but known for low n.
        K_groups.append(numerators[((i+2) // 4)-1])
    elif i%8 == 3:
        K_groups.append(2*(denominators[((i+1) // 4)-1]))
    elif i%8 == 7:
        K_groups.append(denominators[((i+1) // 4)-1])

with open("K_groups.txt", "w") as f:
            f.write(str(K_groups))