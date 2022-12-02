#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:09:36 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re
from anytree import Node, RenderTree
import networkx as nx
from anytree import Node, RenderTree
  
import sys 
link = 'https://adventofcode.com/2020/day/10/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n')


  
file = open('test_input.txt')
file = file.read()
site_content = file.split('\n')[:-1]

site_content = [int(x) for x in site_content]
site_content.sort()

one_jolt = 1
two_jolts = 1
three_jolts = 1

for i in range(0, len(site_content)):
    first = site_content[i]
    second = site_content[i+1]
    
    differnence = second-first
    
    if differnence == 1:
        one_jolt +=1
        
    elif differnence == 2:
        print('ima')
        two_jolts += 1
        
    else:
        three_jolts +=1
       
        
#part 2        
#test data  




