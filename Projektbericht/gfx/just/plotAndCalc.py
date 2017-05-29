#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:17:42 2017

@author: seriousd
"""

import pandas as pd
import numpy as np

import matplotlib as mpl
mpl.use("pgf")
pgf_with_rc_fonts = {
    "font.family": "serif",
    "font.serif": [],                   # use latex default serif font
    "font.sans-serif": ["DejaVu Sans"], # use a specific sans-serif font
}
mpl.rcParams.update(pgf_with_rc_fonts)



import matplotlib.pyplot as plt


plt.figure(figsize=(4.5,2.5))
name = "30kV"


fixed_df = pd.read_csv('30kV.csv', sep='\t', encoding='utf8')
x = fixed_df['U1']
y = fixed_df['U2']

fig = plt.figure()
A = np.vstack([x, np.ones(len(x))]).T
w1 = np.linalg.lstsq(A,y)[0] # obtaining the parameters
print(w1[0],w1[1])
reg1 = w1[0]*x + w1[1]
fig.suptitle(r'Messung 9,89 k\Omega')
plt.xlabel(r'U_1/V')
plt.ylabel(r'U_2/V')

plt.plot(x,y,'.',x,reg1,'r-')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.show()
fig.savefig('plot{}.pdf'.format(name))
fig.savefig('plot{}.pgf'.format(name))

text_file = open("plot{}.tex".format(name), "w")
text_file.write(fixed_df.to_latex())
text_file.close()

name= "100kV"
fixed_df = pd.read_csv('100kV.csv', sep='\t', encoding='utf8')
x = fixed_df['U1']
y = fixed_df['U2']

fig = plt.figure()
A = np.vstack([x, np.ones(len(x))]).T
w2 = np.linalg.lstsq(A,y)[0] # obtaining the parameters
print(w2[0],w2[1])
reg2 = w2[0]*x + w2[1]
fig.suptitle(r'Messung 2,97  k\Omega')
plt.xlabel(r'U_1/V')
plt.ylabel(r'U_2/V')

plt.plot(x,y,'.',x,reg2,'r-')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.show()
fig.savefig('plot{}.pdf'.format(name))
fig.savefig('plot{}.pgf'.format(name))

text_file = open("plot{}.tex".format(name), "w")
text_file.write(fixed_df.to_latex())
text_file.close()
