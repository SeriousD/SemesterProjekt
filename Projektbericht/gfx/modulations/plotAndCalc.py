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
"axes.linewidth" : 0.5,
"axes.titlesize" : 9
}
mpl.rcParams.update(pgf_with_latex)

import matplotlib.pyplot as plt

# I make my own newfig and savefig functions
def newfig(width):
	plt.clf()
	plt.grid(True)
	fig = plt.figure(figsize=figsize(width))
	ax = fig.add_subplot(311)
	return fig, ax
	
def savefig(filename):
	plt.tight_layout(.4)
	plt.savefig('{}.pgf'.format(filename))
	plt.savefig('{}_Preview.pdf'.format(filename))


# Simple plot


def computeCSV(csvInput):
	data = pd.read_csv("{}.csv".format(csvInput), sep=',', encoding='utf8',header=None)
	t = data.iloc[0:,0]	
	x = data.iloc[0:,1]
	y = data.iloc[0:,2]
	c = data.iloc[0:,3]
	

	return t,x,y,c


#========================== Frequency Modulation ==============================
t,x,y,c = computeCSV("FM")

fig, ax = newfig(1)
ax.set_ylim(ymin=-15,ymax=15)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])
ax.set_ylabel('$u_{m}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Nachrichtensignal")
ax.plot(t,x,'C0-')
ax.grid(True)

ax = fig.add_subplot(312)
ax.set_ylim(ymin=-6,ymax=6)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])

ax.set_ylabel('$u_{c}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Trägersignal")
ax.plot(t,y,'C1-')
ax.grid(True)

ax = fig.add_subplot(313)
ax.set_ylim(ymin=-6,ymax=6)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])

ax.set_ylabel('$u_{fm}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Frequenzmoduliertes Signal")
ax.plot(t,c,'C2-')
ax.grid(True)

savefig('FM') 

#========================== Amplitude Modulation ==============================
t,x,y,c = computeCSV("AM")

fig, ax = newfig(1)
ax.set_ylim(ymin=-15,ymax=15)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])
ax.set_ylabel('$u_{m}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Nachrichtensignal")
ax.plot(t,x,'C0-')
ax.grid(True)

ax = fig.add_subplot(312)
ax.set_ylim(ymin=-6,ymax=6)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])

ax.set_ylabel('$u_{c}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Trägersignal")
ax.plot(t,y,'C1-')
ax.grid(True)

ax = fig.add_subplot(313)
ax.set_ylim(ymin=-30,ymax=30)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])

ax.set_ylabel('$u_{am}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Amplitudenmoduliertes Signal")
ax.plot(t,c,'C2-')
ax.grid(True)

savefig('AM') 

#========================== Pulsewidth Modulation ==============================
t,x,y,c = computeCSV("PWM")

fig, ax = newfig(1)
ax.set_ylim(ymin=-15,ymax=15)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])
ax.set_ylabel('$u_{m}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Nachrichtensignal")
ax.plot(t,x,'C0-')
ax.grid(True)

ax = fig.add_subplot(312)
ax.set_ylim(ymin=-15,ymax=15)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])

ax.set_ylabel('$u_{c}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Trägersignal")
ax.plot(t,y,'C1-')
ax.grid(True)

ax = fig.add_subplot(313)
ax.set_ylim(ymin=-0.25,ymax=1.25)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])

ax.set_ylabel('$u_{pwm}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Pulsweiten Signal")
ax.plot(t,c,'C2-')
ax.grid(True)

savefig('PWM') 


#========================== Pulsewidth Modulation ==============================
data = pd.read_csv("PWMarea.csv", sep=',', encoding='utf8',header=None)
t = data.iloc[0:,0]	
y = data.iloc[0:,1]

plt.clf()
plt.grid(True)
fig = plt.figure(figsize=figsize(0.8))
ax = fig.add_subplot(111)
ax.set_ylim(ymin=-0.25,ymax=1.25)
ax.set_xlim(xmin=t.iloc[0],xmax=t.iloc[-1])
ax.set_ylabel('$u_{pmw}/V')
ax.set_xlabel('$t/s$')
ax.set_title("Pulsweitenmoduliertes Signal")
ax.fill_between(t, 0, y,alpha=0.5)
ax.plot(t,y,'-')
ax.grid(True)


savefig('PWMarea') 



