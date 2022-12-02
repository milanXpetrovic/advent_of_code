#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:23:31 2020

@author: ice-cream
"""
from urllib.request import Request, urlopen
import re
from re import search
import pandas as pd 

link = 'https://adventofcode.com/2020/day/4/input'

q = Request(link)

q.add_header('Cookie', 'session=53616c7465645f5f433347e50e3606e81c72e732a2f3cab92eb4c36452aa6eb87ce4b4845a9000facff43da3251244b9; _ga=GA1.2.1290875805.1607369375; _gid=GA1.2.262837703.1607369375')
r = urlopen(q)

site_content = r.read().decode("utf-8")[:-1] .split('\n\n')#[:-1] 

## part 1
dict_list = [] 
counter = 0
for passport in site_content:
    passport = passport.replace('\n', ' ') 
    passport = passport.split(" ")
    
    d = dict(x.split(":") for x in passport)
    dict_list.append(d)

df = pd.DataFrame(dict_list)
df = df.drop('cid', axis=1)
df = df.dropna()
valid_pass = len(df)


## part 2

df['byr'] = pd.to_numeric(df['byr'])
mask = (df['byr'] >= 1920) & (df['byr'] <= 2002)
df = df[mask]

df['iyr'] = pd.to_numeric(df['iyr'])
mask = (df['iyr'] >= 2010) & (df['iyr'] <= 2020)
df = df[mask]

df['eyr'] = pd.to_numeric(df['eyr'])
mask = (df['eyr'] >= 2020) & (df['eyr'] <= 2030)
df = df[mask]


mask = df['hcl'].str.match('^#[a-f0-9]{6}$')== True
df = df[mask]

mask = df['ecl'].str.contains('(amb|blu|brn|gry|grn|hzl|oth)')== True
df = df[mask]

mask = df['pid'].str.match('^[0-9]{9}$')== True
df = df[mask]

mask=df['hgt'].str.contains(r'(\d*)(in|cm)')
df = df[mask]

mask = df['hgt'].str.contains(r'cm$')
df1 = df[mask]

df1['hgt'] = df1['hgt'].str.replace(r'cm$', '')
df1['hgt'] = pd.to_numeric(df1['hgt'])
mask = (df1['hgt'] >= 150) & (df1['hgt'] <= 193)
df1 = df1[mask]

mask = df['hgt'].str.contains(r'in$')
df2 = df[mask]

df2['hgt'] = df2['hgt'].str.replace(r'in$', '')
df2['hgt'] = pd.to_numeric(df2['hgt'])
mask = (df2['hgt'] >= 59) & (df2['hgt'] <= 76)
df2 = df2[mask]

df = pd.concat([df1, df2], axis = 0)



