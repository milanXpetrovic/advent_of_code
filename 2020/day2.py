#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:52:18 2020

@author: ice-cream
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:31:24 2020

@author: ice-cream
"""
import re
from urllib.request import Request, urlopen

link = 'https://adventofcode.com/2020/day/2/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8").split('\n')[:-1] 


## part 1

counter = 0
for line in site_content:
    lowest_num, highest_num, letter, pattern = re.split('-| |: ', line)
    
    letter_count = pattern.count(letter) 
    
    if letter_count >= int(lowest_num) and letter_count <= int(highest_num):
        counter +=1


#part 2 
counter = 0
for line in site_content:
    position1, position2, letter, pattern = re.split('-| |: ', line)
    pos1 = int(position1) - 1
    pos2 = int(position2) - 1
    
    letter_pos1 = pattern[pos1]
    letter_pos2 = pattern[pos2]
    
    if letter_pos1 == letter or letter_pos2 == letter:
        if letter_pos1 != letter_pos2:
            counter += 1
        
        
        
        
        