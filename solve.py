from cube_rings import *
from cube import *

class Solve():
	def __init__(self, scramble):
		self.scramble = scramble
		self.scrambled, self.solved = Cube(), Cube() #two states of a cube
		self.scrambled.scrambling(self.scramble, ring)

		self.find_solved_elements()
		self.find_flips()
		self.memo()
		self.summary()


	def find_solved_elements(self):
		self.solved_edges, self.solved_corners = 0,0
		self.solved_groups = []
		for target in self.solved.groups:
			if self.solved.stickers[target] == self.scrambled.stickers[target] and self.solved.stickers[target] != 'buffer':
				self.solved_groups.append(target)
				if len(target) == 2: self.solved_edges += 1
				else: self.solved_corners += 1
	
	#finds flips and twists
	def find_flips(self):
		self.flips, self.twists = 0,0
		self.flipped_groups = []
		for target in self.solved.groups:
			solved_state, scrambled_state = [], []
			for sticker in self.solved.groups[target]:
				#print(self.solved.stickers[sticker], self.scrambled.stickers[sticker])
				solved_state.append(self.solved.stickers[sticker])
				scrambled_state.append(self.scrambled.stickers[sticker])
			if sorted(solved_state) == sorted(scrambled_state) and solved_state != scrambled_state:
				self.flipped_groups.append(target)
				if len(solved_state) == 2: self.flips += 1
				else: self.twists += 1
			else: continue

	#method returns key of dictionary by the value
	#used mainly in memo() to find another target
	def return_target(self, letter, type_of_element):
		if type_of_element == 'c': length = 3
		else: length = 2
		for target in self.scrambled.stickers:
			if self.solved.stickers[target] == letter and length == len(target): 
				for group in self.solved.groups:
					if target in self.solved.groups[group]:
						return target, group
			

	def memo(self):
		self.edges_memo_cycle = ['UF']
		self.corners_memo_cycle = ['UFR']
		self.memorized_edges, self.memorized_corners = [], []
		self.edge_breaks, self.corner_breaks = 0, 0

		'''
		two similar loops below, but corners are harder to implement, so I didn't want to remove a little redundancy 
		'''


		#egdes

		memoed = [] #memorized group of targets, eg. FL stands for FL and LF
		place_of_break = '' #group of tagret which breaks the cycle
		for current_target in self.edges_memo_cycle: #looping through cycle
			target_sticker = self.scrambled.stickers[current_target]
			if target_sticker == 'buffer' or self.return_group(current_target) == place_of_break:
				target = self.find_free_target(memoed, 'e')
				if target == None:
					break
				else:
					self.edge_breaks += 1
					self.memorized_edges.append(self.solved.stickers[target])
					place_of_break = target
					self.memorized_edges.append(self.scrambled.stickers[target])
					target_sticker = self.scrambled.stickers[target]
					next_target, grp = self.return_target(target_sticker, 'e')
					self.edges_memo_cycle.append(next_target)
					memoed.append(grp)
					continue
			else:
				self.memorized_edges.append(target_sticker)
				next_target, grp = self.return_target(target_sticker, 'e')
				self.edges_memo_cycle.append(next_target)
				memoed.append(grp)


		#corners
		place_of_break = ''
		for current_target in self.corners_memo_cycle:
			target_sticker = self.scrambled.stickers[current_target]
			#print(current_target, self.return_group(current_target), place_of_break)
			if target_sticker == 'buffer' or self.return_group(current_target) == place_of_break:
				target = self.find_free_target(memoed, 'c')
				if target == None:
					break
				else:
					self.corner_breaks += 1
					self.memorized_corners.append(self.solved.stickers[target])
					place_of_break = target
					self.memorized_corners.append(self.scrambled.stickers[target])
					target_sticker = self.scrambled.stickers[target]
					next_target, grp = self.return_target(target_sticker, 'c')
					self.corners_memo_cycle.append(next_target)
					memoed.append(grp)
					continue
			else:
				self.memorized_corners.append(target_sticker)
				next_target, grp = self.return_target(target_sticker, 'c')
				self.corners_memo_cycle.append(next_target)
				memoed.append(grp)

	#find unsolved group on the cube
	def find_free_target(self, memoed, type_of_element):
		if type_of_element == 'c': length = 3
		else: length = 2
		for target in self.solved.groups:
			if target == 'UF' or target == 'UFR' or len(target) != length: continue
			if target not in memoed+self.solved_groups+self.flipped_groups:
				return target
		return None

	#returns group of the target
	def return_group(self, target):
		for group in self.solved.groups:
			if target in self.solved.groups[group]:
				return group
	
	#method generates as many apostrophes as many flipped or twisted elements are in the scramble
	@staticmethod
	def apostrophes(elements):
		c_index, e_index = '', ''
		for target in elements:
			if len(target) == 2:
				e_index += "'"
			else:
				c_index += "'"
		return e_index, c_index

	#prints basics info about the solve
	def summary(self):
		self.corner_targets = len(self.memorized_corners)
		self.edge_targets = len(self.memorized_edges)
		self.flipped_elements = len(self.flipped_groups)

		if self.edge_targets%2 == 0 or self.memorized_edges[-1] == 'G':
			self.algorithms = int(self.flipped_elements + (self.corner_targets + self.edge_targets)/2 )
		else:
			self.algorithms = int(1 + self.flipped_elements + (self.corner_targets + self.edge_targets)/2 )

		flips_index, twists_index = self.apostrophes(self.flipped_groups)
		

		print("{}{}/{}{}".format(self.edge_targets, flips_index, self.corner_targets, twists_index))
		print("algs:", self.algorithms)
		print()
		print("edges:", self.edge_targets, self.memorized_edges)
		print("corners:", self.corner_targets, self.memorized_corners)
		print()
		print("solved elements: ", self.solved_groups)
		print("solved edges: {}\nsolved corners: {}".format(self.solved_edges, self.solved_corners))
		print()
		print("flipped elements: ", self.flipped_groups)
		print("flips: {}\ntwists: {}".format(self.flips, self.twists))
		print()
		print("number of cycle breaks: {} ({}+{})".format(self.edge_breaks+self.corner_breaks, self.edge_breaks, self.corner_breaks))



ring = Ring()
scramble = "R U R' U'"
current_solve = Solve(scramble) #scramble is an argument of the constructor






