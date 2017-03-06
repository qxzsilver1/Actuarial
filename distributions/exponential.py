import numpy as np
import scipy as sp
import statsmodels as sm
import matplotlib as mpl
import pandas as pd

# returns the function definition of:
# pdf = lambda * exp(-lambda * x)

class Exponential(object):
    def __init__(self, lambda, loc = 0):
        self.lambda = lambda
        self.loc = loc

    def pdf(x):
        return sp.stats.expon.pdf(x, self.loc, 1/self.lambda)

    def cdf(x):
        return sp.stats.expon.cdf(x, self.loc, 1/self.lambda)

    def sf(x):
        return sp.stats.expon.sf(x, self.loc, 1/self.lambda)
        
    def mean():
        return 1/self.lambda
        
    def variance():
        return 1/(self.lambda ** 2)
        
    def std_dev():
        return 1/self.lambda
    

    

