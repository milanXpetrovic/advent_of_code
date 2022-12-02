#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Thu Dec 10 12:09:25 2020

from urllib.request import Request, urlopen
import re
from anytree import Node, RenderTree
import networkx as nx
from anytree import Node, RenderTree

link = 'https://adventofcode.com/2020/day/8/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1].split('\n')#[:-1] 

"""
#test data       
file = open('test_input.txt')
file = file.read()
site_content = file.split('\n')[:-1]
#site_content[7] = 'nop -4' 
  


index = 0 
accumulator = 0
checked_list = []

while True:
    if index in checked_list:
        print('value before break:',accumulator)
        break
    
    checked_list.append(index)
    command = site_content[index].split(' ')
    
    input_command = command[0]
    value = int(command[1])
    
    if input_command == 'acc':
        accumulator += value
        index += 1    

            
    elif input_command == 'jmp':
        index += value

    
    else:
        index += 1

    #print(accumulator)
"""
#part 2 
index = 0 
accumulator = 0
checked_list = []

#site_content[7] = 'nop +1'



jmp_locations = []
nop_locations = [] 

counter = 0
for inputs in site_content:
    command = inputs.split(' ')
    input_command = command[0]
    value = int(command[1])

    if input_command == 'jmp':
        jmp_locations.append(counter)
    
    if input_command == 'nop':
        nop_locations.append(counter)
        
    counter +=1


for jmp_index in jmp_locations:
    r = urlopen(q)

    site_content = r.read().decode("utf-8")[:-1].split('\n')#[:-1] 
    
    site_content[jmp_index] = 'nop +1'
    
    index = 0 
    accumulator = 0
    checked_list = []
    try: 
        while True:
            if index in checked_list:
               #print('value before break:',accumulator)
                break
            
            checked_list.append(index)
            command = site_content[index].split(' ')
            
            input_command = command[0]
            value = int(command[1])
            
            if input_command == 'acc':
                accumulator += value
                index += 1    
        
                    
            elif input_command == 'jmp':
                index += value
        
            
            else:
                index += 1
        
            
    
    except IndexError:
        print(accumulator)
