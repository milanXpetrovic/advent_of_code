#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:15:57 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re
from anytree import Node, RenderTree
import networkx as nx
from anytree import Node, RenderTree
  
import sys 
link = 'https://adventofcode.com/2020/day/9/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n')

#test data  
"""     
file = open('test_input.txt')
file = file.read()
site_content = file.split('\n')[:-1]
"""

## part 1
site_content = [int(x) for x in site_content]

def check_if_valid(list_to_check):
    all_sums = []
    for numb1 in list_to_check:
        for numb2 in list_to_check:
            all_sums.append(numb1+numb2)

    return list(set(all_sums))

    
  
index_counter = 0 
step = 25

found_nums = []

for i in range(step, len(site_content)):

    list_to_check = site_content[i:i+step]
    
    all_sums = check_if_valid(list_to_check)
    
    if site_content[i + step] not in all_sums:
        print(site_content[i + step])
        break
 
#585


## part 2 
goal = 167829540    

values = []
for i in range(0, len(site_content)):
    
    total = 0
    numbers_to_check = site_content[i:]
    
    numbers_cache = []
    for number in numbers_to_check:
        total += number
        numbers_cache.append(number)
        if total == goal:
            print(len(numbers_cache))
            print(min(numbers_cache)+max(numbers_cache))
            break
        if total > goal:
            break
            





    
    
    