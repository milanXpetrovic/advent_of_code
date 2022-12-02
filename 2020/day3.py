#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:19:04 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen

link = 'https://adventofcode.com/2020/day/3/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8").split('\n')[:-1] 

index = 0 
slope = 3 

#site_content = '..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#\n'
#site_content = site_content.split('\n')[:-1]

#part 1
"""
tree_counter = 0
for line in site_content:
    
    if index >= len(line):
        index = index-len(line)
        
    if line[index] == '#':
        tree_counter += 1
        
    index = index+slope
""" 
#part 2 

slopes = [1, 3, 5, 7]
tree_counts = []

for slope in slopes:
    index = 0
    tree_counter = 0
    for i in range(0, len(site_content)):
        line = site_content[i]
        
        if index >= len(line):
            index = index-len(line)
        
        if line[index] == '#':
            tree_counter += 1
            
        index = index+slope
    
    tree_counts.append(tree_counter)
    
    
index = 0
slope = 1
tree_counter = 0
for i in range(0, len(site_content), 2):
    line = site_content[i]
    
    if index >= len(line):
        index = index-len(line)
    
    if line[index] == '#':
        tree_counter += 1
        
    index = index+slope
    
tree_counts.append(tree_counter)

res=1
for x in tree_counts:
    res = res*x




