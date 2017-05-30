#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:17:42 2017

@author: seriousd
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('pgf')

def figsize(scale):
	fig_width_pt = 390.0 #469.755 # Get this from LaTeX using \the\textwidth
	inches_per_pt = 1.0/72.27 # Convert pt to inch
	golden_mean = (np.sqrt(5.0)-1.0)/2.0 # Aesthetic ratio (you could change this)
	fig_width = fig_width_pt*inches_per_pt*scale # width in inches
	fig_height = fig_width*golden_mean # height in inches
	fig_size = [fig_width,fig_height]
	return fig_size
	
pgf_with_latex = { # setup matplotlib to use latex for output
"pgf.texsystem": "pdflatex", # change this if using xetex or lautex
"text.usetex": True, # use LaTeX to write all text
"font.family": "serif",
"font.serif": [], # blank entries should cause plots to inherit fonts from the document
"font.sans-serif": [],
"font.monospace": [],
"axes.labelsize": 10, # LaTeX default is 10pt font.
"font.size": 10,
"legend.fontsize": 8, # Make the legend/label fonts a little smaller
"xtick.labelsize": 8,
"ytick.labelsize": 8,
"figure.figsize": figsize(0.9), # default fig size of 0.9 textwidth
"pgf.preamble": [
r"\usepackage[utf8x]{inputenc}", # use utf8 fonts becasue your computer can handle it :)
r"\usepackage[T1]{fontenc}", # plots will be generated using this preamble
],
"grid.alpha" : 0.5,
"grid.linestyle" : ":",
"grid.color" : "#000000",
"grid.linewidth" : 0.5,
"lines.linewidth" : 0.75,
"axes.linewidth" : 0.5
}
mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt

# I make my own newfig and savefig functions
def newfig(width):
	plt.clf()
	fig = plt.figure(figsize=figsize(width))
	ax = fig.add_subplot(111)
	return fig, ax
	
def savefig(filename):
	plt.grid(True)
	plt.tight_layout(.4)
	plt.savefig('{}.pgf'.format(filename))
	plt.savefig('{}_Preview.pdf'.format(filename))


# Simple plot


def calcRegression(csvInput,forceOrigin=False):
	fixed_df = pd.read_csv("{}.csv".format(csvInput), sep='\t', encoding='utf8')
	x = fixed_df['U1']
	y = fixed_df['U2']
	if forceOrigin is False:
		ori=1
	else:
		ori=0
	
	A = np.vstack([x, ori*np.ones(len(x))]).T
	w = np.linalg.lstsq(A,y)[0] # obtaining the parameters
	m = w[0]
	b = w[1]
	print("Regression: y={}x {}".format(m,b))
	reg = m*x + b

	tex_table = open("{}_TexTable.tex".format(csvInput), "w")
	tex_table.write(fixed_df.to_latex())
	tex_table.close()

	return x,y,reg


#9k89 File
fig, ax = newfig(1)

x,y,reg = calcRegression("9k89",forceOrigin=True)
ax.set_ylim(ymin=0,ymax=32)
ax.set_xlim(xmin=0,xmax=2.2)
ax.set_xlabel('$U_1$/V')
ax.set_ylabel('$U_2/V$')


ax.plot(x,y,'x',label="Messwerte")
ax.plot(x,reg,'-',label="Regressionsgrade")
plt.legend()

savefig('9k89') 

#2k97 File
fig, ax = newfig(1)

x,y,reg = calcRegression("2k97",forceOrigin=True)
ax.set_ylim(ymin=0,ymax=105)
ax.set_xlim(xmin=0,xmax=2.2)
ax.set_xlabel('$U_1$/V')
ax.set_ylabel('$U_2/V$')
ax.plot(x,y,'x',label="Messwerte")
ax.plot(x,reg,'-',label="Regressionsgrade")
plt.legend()
savefig('2k97')






