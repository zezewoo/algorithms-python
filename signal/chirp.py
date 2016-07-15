#! /usr/bin/python

from pylab import *
import numpy as ny


f = 20*1000
A = 9



t = ny.arange(0,100,0.01)
s = sin(t)

plot(t, s)
show()