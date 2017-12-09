
# coding: utf-8

# In[1]:

#Import libraries
import scipy.stats as stat
import numpy as np
from __future__ import division
get_ipython().magic(u'matplotlib inline')


# Question 1

# Part A

# In[3]:

#Function to compute the premium
def Premium(U,q,eta):
    return (1+eta)*U*q;


# Part B

# In[4]:

print Premium(1000,0.1,0.05)


# Question 2

# Part A

# In[6]:

#Ruin Probability Function
def RuinCLT( n,u,U,q,eta ):
    p = Premium(U,q,eta)
    ruinprob = 1-stat.norm.cdf((n/(q*(1-q)))**(0.5)*((u+n*p)/n/U-q))
    return ruinprob


# Part B

# In[8]:

n = 10000 #Number of policy holders
u = 200 #Initial reserves
U = 1000 #Cost of each claim for the insurance company
q = 0.1 #Probability of a car accident
eta =0.05 #Safety loading
p = Premium( U,q,eta )#Premium
print RuinCLT( n,u,U,q,eta )


# Question 3

# Part A

# In[9]:

#Function to determine the initial reserve for a given risk level using the def InitialCapital( n,alpha,q,U,eta ):
def InitialCapital( n,alpha,q,U,eta ):
    p = Premium(U,q,eta)
    intialres = (((q*(1-q))/n)**(0.5)*stat.norm.ppf(1-alpha)+q)*n*U-n*p
    return intialres


# Part B

# In[10]:

n = 10000 #Number of policy holder
u = 200 #Initial reserves
U = 1000 #Cost of each claim for the insurance company
q = 0.1 #Probability of a car accident
eta = 0.05 #Safety loading
p = Premium(U,q,eta) #Premium
#Part a) is iterated a thousand times
#Create an empty list
ruins = []
for k in range(1,1000,1):
    #Indicates which policy holder suffered from a car accident
    X = np.random.binomial(1,q,n)
    #Computate financial reserve 
    #Check if the reserve is positive (no ruin) or negative (ruin)
    reserve = u+n*p-U*np.sum(X)
    ruin = reserve<0
    ruins.append(ruin) #Print the reserve
    

#the Monte Carlo approximation of the ruin probability
print sum(ruins)/1000


# Question 5 Calculating the exact value of the ruin probability

# Part A

# In[12]:

def ExactRuinProbability(u,n,U,q,eta):
    p = Premium(U,q,eta)
    ruinprob = 1-stat.binom.cdf((u+n*p)/U,n,q)
    return ruinprob


# Part B

# In[13]:

n = 10000 #Number of policy holder
u = 200 #Initial reserves
U = 1000 #Cost of each claim for the insurance company
q = 0.1 #Probability of a car accident
eta = 0.05 #Safety loading
p = Premium( U,q,eta )#Premium
print ExactRuinProbability(u,n,U,q,eta)


# Question 6

# Increasing the number of customers in the portfolio will improve the CLT approximation. Increasing the number of times the experiment is repeated will improve the Monte Carlo approximation. 
