import numpy as np
import pandas as pd
import scipy.stats as stats
import statistics
import math
import matplotlib.pyplot 

#number of hypotetical values for normalized mean
elements=400
#number of values used to take one value of normalized mean
capacity=200
#ditribution, choose between: binom, negbinom, poisson or hypge
dist='poisson'
#run and plot a normal dist no matter the previous choice

#'meano' is always mean and 'varia' is the variance

if dist=='binom':
    #number of tries
    num=5
    #probability of success
    prob=.5
    #list of number of success in 'n' trials
    Y=stats.binom.rvs(size=elements*capacity, n=num, p=prob)
    meano=num*prob
    varia=num*prob*(1-prob)
    #for probability of value 'k' use: binom.pmf(k, num, prob)
    
if dist=='negbinom':
    #number of success wanted
    suc=2
    #probability to get a success in one trial
    prob=.5
    #list of number of trial to get 'suc' success
    Y=stats.nbinom.rvs(suc, p=prob, size=elements*capacity)
    meano=suc*(1-prob)/prob
    varia=suc*(1-prob)/(prob**2)
    #for probability of value 'k' use: nbinom.pmf(k,suc,prob)

if dist=='hypge':
    #total candy 
    T = 60
    #total chocolate
    C= 24
    #how many can we pick?
    num = 7
    #list of chocolate we got after getting 'num' candy from a bag with 'T' candy and 'C' chocolates
    Y=stats.hypergeom.rvs(T, C, num, size=elements*capacity)
    #first draw prob of getting chocolate
    prob=C/T
    #mean as binom, but the variance is perturbed
    meano=num*prob
    varia=num*prob*(1-prob)*(T-C)/(T-1)
    #for probability of value 'k' use: hypergeom.pmf(k, T, C, num)
    
if dist=='poisson':
    #Poisson dist only depends on the mean
    meano=1
    Y=stats.poisson.rvs(meano, size=elements*capacity)
    varia=meano
    #for probability of value 'k' use: poisson.pmf(k,meano)

#the number of values for the noralized means is 'elements'
#the normalized mean is: ( (the mean of 'capacity' values)-(meano) )/ sqrt(varia/capacity)

nY = [math.sqrt(capacity/varia)*(float(x)-meano) for x in Y]

EY=[statistics.mean(nY[i*capacity:(i+1)*capacity]) for i in range(elements)]

pd.DataFrame(EY).hist(range=(-6,6), bins=30);