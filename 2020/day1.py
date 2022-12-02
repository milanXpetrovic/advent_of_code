#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:31:24 2020

@author: ice-cream
"""

from urllib.request import Request, urlopen

link = 'https://adventofcode.com/2020/day/1/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8").split('\n')[:-1] 

site_content_int = [int(x) for x in site_content]

#part 1
for x in site_content_int:
    for y in site_content_int:
        if x + y == 2020:
            print(x*y)
    


#part 2
for x in site_content_int:
    for y in site_content_int:
        for z in site_content_int:
            if x + y + z == 2020:
                print(x*y*z)