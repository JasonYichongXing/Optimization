#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:13:29 2018

@author: xingyichong
"""
from scipy.optimize import minimize 

#1. Quadratic Programming
myfun = lambda x: 1.5*x[0]**2 - 3*x[3]*x[0] + x[1]**2 - 2*x[2]  
mycons = ({'type': 'ineq', 'fun': lambda x: x[0]+x[1]+2*x[2]-15},
          {'type': 'eq', 'fun': lambda x: 15 - sum([x**2 for x in x])})

Bi2 = (-10,10)
Bnds2 = (Bi2,Bi2,Bi2,Bi2)

sol1 = minimize(myfun,[1,1,1,1],method='SLSQP',bounds=Bnds2,constraints=mycons)
print('----LS QP----\n',sol1)
    
