#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:27:03 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re

link = 'https://adventofcode.com/2020/day/6/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n\n')#[:-1] 

# part 1
total_sum = 0
for group_ans in site_content:
    group_ans = group_ans.replace("\n", "")
    group_ans = group_ans.replace(" ", "")
    group_ans = set(group_ans)
    total_sum = total_sum + len(group_ans)

# part 2 

#site_content = 'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'
#site_content = site_content.split('\n\n')

total_sum = 0

check = []
for group_ans in site_content:
    group_ans = group_ans.split("\n")
    
    result_set = set(group_ans[0])
    
    group_ans = group_ans[1:]
    
    for s in group_ans:
        result_set.intersection_update(s)
 
    total_sum = total_sum + len(result_set)
    



