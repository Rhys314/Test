# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:14:28 2016
Test script.
@author: Rhys Poolman
"""
import spiceypy as spice
import plotly
import plotly.offline as py
import plotly.graph_objs as go

# print out the toolkit version
print(spice.tkvrsn('TOOLKIT'))

spice.furnsh('./cassini_kernel/cassMetaK.txt')

step = 4000

# we are going to get positions between these two dates
utc = ['Jun 20, 2004', 'Dec 1, 2005']

# get et values one and two, we could vectorize str2et
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
print('Et One: {}, ET Two: {}'.format(etOne, etTwo))

# get times
times = [x*(etTwo - etOne)/step + etOne for x in range(step)]

# check first few times
print(times[0:3])

# run spkpos as a vectorized function
positions, lightTimes = spice.spkpos('Cassini', times, 'J2000', 'NONE',
                                     'SATURN BARYCENTER')

# positions in a 3xN vector or XYZ positions
print('Positions: ')
print(positions[0])

# light times is a N vector of time
print('Light times: ')
print(lightTimes[0])

# clean up the kernels
spice.kclear()

# plot
plotly.offline.init_notebook_mode()
threeDPlot = go.Scatter3d(x=positions[:, 0],  # X coordinates
                          y=positions[:, 1],  # Y coordinates
                          z=positions[:, 2],  # Z coordinates
                          name='Cassini',
                          mode='lines',
                          line=dict(width=3))

barycenter = go.Scatter3d(x=[0],
                          y=[0],
                          z=[0],
                          name='bc',
                          mode='marker',
                          marker=dict(size=10, color='orange'))

data = [threeDPlot, barycenter]

layout = go.Layout(title="SpiceyPy Cassini Position Example")

fig = dict(data=data, layout=layout)
py.iplot(fig)
