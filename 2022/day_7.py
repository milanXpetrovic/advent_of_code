with open('test_input.txt', 'r') as f:
	a = f.read().split("\n")


class Dir:
	def __init__(self, name, parent):
		self.name = name
		self.size = 0
		self.files = []
		self.children = []
		self.parent = parent

	def add_file(self, file):
		self.files.append(file)

	def add_children(self, file):
		self.children.append(file)

	def get_size(self):
		if len(self.children) != 0:
			for child in self.children:
				child.get_size()
			
			for child in self.children:
				self.size += child.size

			self.size += sum(self.files)

		else:	
			self.size=sum(self.files)


node = Dir("\\", None)
root = node
for s in a:
	s = s.split(" ")

	if len(s) == 3 and s[1] == "cd" and s[2] != "..":
		# cd to dir
		new_node = Dir(s[2], node)
		node.add_children(new_node)
		node=new_node

	if len(s) == 2 and s[0] != "dir" and s[1] != "ls":
		# file in dir sizes
		size = int(s[0])
		node.add_file(size)
		pass
		
	if len(s) == 3 and s[1] == "cd" and s[2] == "..":
		# going up
		node = node.parent

root.get_size()

visit = root.children
temp = float('inf')
while visit:
	node = visit.pop()

	if node.size >= 30000000-(70000000-root.size) and node.size <= temp:
		temp = node.size

	for c in node.children:
		visit.append(c)

print(temp)