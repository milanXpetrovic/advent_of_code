import re
from urllib.request import Request, urlopen


def get_data(DAY):
	link = 'https://adventofcode.com/2021/day/'+ str(DAY) +'/input'
		
	q = Request(link)

	q.add_header('Cookie', 'session=53616c7465645f5f25db6ae82413a4de9a03f13bba2696a4c0039eb06cc3f24609eebfb60bcf65c489ff69c66117f340')
	r = urlopen(q)
	
	site_content = r.read().decode("utf-8").split('\n')[:-1] 

	return site_content


def list_elem_to_int(list_of_str):
	return [int(x) for x in list_of_str]