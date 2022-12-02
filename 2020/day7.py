#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 01:50:58 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re
from anytree import Node, RenderTree
import networkx as nx
from anytree import Node, RenderTree

link = 'https://adventofcode.com/2020/day/7/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n')#[:-1] 

"""
above_nodes = []
lines = []

for line in site_content:
    
    line = line.replace(".", "").replace("contain", ",")
    line = line.replace('bags ', '').replace('bags', '')
    line = line.replace('bag ', '').replace('bag', '')
    line = re.sub(' [0-9]', '',line).strip()
    line = line.replace(" ", "")
    line = line.split(',')
    
    lines.append(line)


above_nodes = []
for line in lines:
    main_bag = line[0]
    content = line[1:]
    if 'shinygold' in content:
        above_nodes.append(main_bag)

for line in lines:
    for line in lines:
        main_bag = line[0]
        content = line[1:]
        
        for bag in content:
            if bag in above_nodes:
                above_nodes.append(main_bag)

    above_nodes = list(set(above_nodes))           

print(len(above_nodes))
"""
##part2 
def get_node_values(bag_item):
    name =  re.sub('[0-9]', '',bag_item).strip()
    
    if name == 'noother':
        print('name')
    
    if len(re.findall(r'\d+', bag_item)) == 0:
        value = 1
        
    else:
        value = re.findall(r'\d+', bag_item)[0]
            
    return name, int(value)

        
#test data       
file = open('test_input.txt')
file = file.read()
site_content = file.split('\n')

#data preproc
lines = []
for line in site_content:
    line = line.replace(".", "").replace("contain", ",")
    line = line.replace('bags ', '').replace('bags', '')
    line = line.replace('bag ', '').replace('bag', '')
    #line = re.sub(' [0-9]', '',line).strip()
    line = line.replace(" ", "")
    line = line.split(',')
    
    lines.append(line)

    

bag_content = []
for line in lines:
    main_bag = line[0]
    content = line[1:]
    if 'shinygold' in main_bag:
        bag_content.append(content)



#above_nodes = list(set(above_nodes))  

    
"""         
#shine_gold_content = []  
#main_bag = line[0]
#content = line[1:]

total = 0

for line in lines:
    main_bag = line[0]
    content = line[1:]
    
    temp = re.findall(r'\d+', main_bag) 
    if len(re.findall(r'\d+', main_bag)) == 0:
        temp = 1
    
    total = total + temp
    
    sum_content = 0 
    
    for element in content:
        num_value = re.findall(r'\d+', element)[0]
        if len(re.findall(r'\d+', element)) == 0:
            num_value = 1
            
        sum_content = sum_content +  int(num_value)
   
    
    content_val = len(content) * sum_content
    
    total = total + content_val
"""                    
                       
                       
    
    
    
    
    
    
    
    