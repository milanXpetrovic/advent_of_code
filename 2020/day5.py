#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 00:55:21 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re
from re import search
import pandas as pd 

link = 'https://adventofcode.com/2020/day/5/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n')#[:-1] 

## part1
B = 1 
F = 0
R = 1 
L = 0

id_list = []
for line in site_content:
    line = line.replace('B', str(1))
    line = line.replace('R', str(1))
    line = line.replace('F', str(0))
    line = line.replace('L', str(0))
    id_list.append(line)
    
id_list = [int(n,2) for n in id_list]
max_id = max(id_list)


## part2
id_list.sort()
list_of_ids = [x-min(id_list) for x in id_list]

counter = 0 
for seat_id in list_of_ids:
    counter +=1
    if seat_id != counter:
        my_seat_id = counter + min(id_list)
        