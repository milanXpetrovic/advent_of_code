#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:21:16 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re
from anytree import Node, RenderTree
import networkx as nx
from anytree import Node, RenderTree
  
import sys 
link = 'https://adventofcode.com/2020/day/11/input'

q = Request(link)
q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n')


grid = []
for line in site_content:
    line = [0 if x=='L' else x for x in line]
    line = [0.001 if x=='.' else x for x in line]
    grid.append(line)
    
    


# Python code to implement Conway's Game Of Life
import argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# setting up the values for the grid
TAKEN = 1
EMPTY = 0
vals = [TAKEN, EMPTY]

def createGrid(N):
    link = 'https://adventofcode.com/2020/day/11/input'
    
    q = Request(link)
    q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
    r = urlopen(q)
    
    site_content = r.read().decode("utf-8")[:-1].split('\n')
        
# =============================================================================
#     file = open('test_input.txt')
#     file = file.read()
#     site_content = file.split('\n')[:-1]     
# =============================================================================

    grid = []
    for line in site_content:
        line = [0 if x=='L' else x for x in line]
        line = [0.001 if x=='.' else x for x in line]
        grid.append(line)

        
    # returns a grid of NxN random values
    return grid



def update(frameNum, img, grid, N):
 
    # copy grid since we require 8 neighbors 
    # for calculation and we go line by line 
    newGrid = grid.copy()
    N = len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
 
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around 
            # so that the simulaton takes place on a toroidal surface.
            total = float((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            
            #print(total)
            # apply Conway's rules
            if grid[i, j]  == EMPTY and total < 0.1:
                newGrid[i, j] = TAKEN
                                 
            elif grid[i, j] == TAKEN and total >= 5:
                newGrid[i, j] = EMPTY
            else:
                newGrid[i, j] = grid[i, j]
                
                
 
    # update data
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j] == TAKEN:
                counter +=1
    print(counter)
    
    img.set_data(newGrid)
    
    
    grid[:] = newGrid[:]
    return img,


# main() function
#def main():
 
# Command line args are in sys.argv[1], sys.argv[2] ..
# sys.argv[0] is the script name itself and can be ignored
# parse arguments
parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
 
# add arguments
parser.add_argument('--grid-size', dest='N', required=False)
parser.add_argument('--mov-file', dest='movfile', required=False)
parser.add_argument('--interval', dest='interval', required=False)
parser.add_argument('--glider', action='store_true', required=False)
parser.add_argument('--gosper', action='store_true', required=False)
args = parser.parse_args()
 
# set grid size
N = 100
if args.N and int(args.N) > 8:
    N = int(args.N)
     
# set animation update interval
updateInterval = 50
if args.interval:
    updateInterval = int(args.interval)
 
# declare grid
grid = np.array([])
 
grid = np.array(createGrid(100))
 
# set up animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                              frames = 10,
                              interval=updateInterval,
                              save_count=50)
 
# # of frames? 
# set output file
if args.movfile:
    ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
 
plt.show()
 
# call main

if __name__ == '__main__':
    main()



