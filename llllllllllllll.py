# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:24:47 2016

@author: sowah
"""

import numpy as np
def factors(n):
    factPrime = []
    fact =[]

    if n == 1:
        return fact, factPrime
    elif n == 2:
        fact.append(1)
        factPrime.append(n)
        return fact, factPrime
    elif n == 3:
        fact.append(1)
        factPrime.append(3)
        return fact, factPrime
    else:
        fact.append(1)
        for i in range(2, n):
            if n % i == 0:
                fact.append(i)
                if primeChecker(i):
                    factPrime.append(i)
                else:
                    continue
            else:
                continue
    return fact, factPrime


def primeChecker(m):
    police = 0
    for i in range(2, m):
        if m % i == 0:
            police += 1
        else:
            continue
    if police == 0:
        return True
    else:
        return False


def typeNumber(myFactors, theNumber):
    if theNumber > 1:
        if sum(myFactors) == theNumber:
            return "is perfect"
        elif sum(myFactors) > theNumber:
            return "is abundant"
        else:
            return "is deficient"
    else:
        return "Error ", theNumber, " Is Out Of Range For This Operation"

# main function goes here

# declaring variables

myPrime = []
myFact = []
myPerfect = []
myDeficient = []
myAbundant = []
myMersenne = []
mySemiperfect = []
a = input("Enter Your a Here :")
a=int(a)
b = input("enter your b Here :")
b=int(b)
if b<a or b<0 or a<0:
    raise ValueError
else:
    for i in range(a,b+1):
        myFact, myPrime = factors(i)
        if typeNumber(myFact,i) == "is deficient":
            myDeficient.append(i)
        elif typeNumber(myFact,i) == "is perfect":
            myPerfect.append(i)
            myMersenne.append(int(((np.log2(1+np.sqrt(1+8*i)))-1)))
        else:
            myAbundant.append(i)
			
for o in myAbundant:
	for j in range(1,o+1):
		A = []      #Sublist of primes less than n
		if primeChecker(j)==True:
			A.append(j)
		else:
			continue
		for a in A:
			m = o/a
			if (m == int(m)) & (2**m > a) & (np.log2(m)==int(np.log2(m))):
                         mySemiperfect.append(o)
			else:
				continue
                 
 #            else:
 #                continue
 #        else:
 #           continue



print ("The Deficient numbers are", myDeficient)
print ("The Abundant numbers are", myAbundant)
print ("The Perfect numbers in order", myPerfect)
print ("The prime that make them mersenne in the same order",myMersenne)
print ("The Semi perfect numbers are", mySemiperfect)
