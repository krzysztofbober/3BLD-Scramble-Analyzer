from cube_moves import *

class Cube:
	rotations = {
	#key - middle move, value - appropriate rotation to back to white green orientation
	'M': 'x',
	'S': 'z',
	'E': 'y',
	#key - rotation, value - moves, that generates rotation
	'x2': ['R2', 'L2', 'M2'],
	'z2': ['F2', 'B2', 'S2'],
	'y2': ['U2', 'D2', 'E2'],
	"x'": ["R'", "L", "M"],
	"y'": ["U'", "D", "E"],
	"z": ["F'", "S'", "B"],
	"x": ["R", "L'", "M'"],
	"y": ["U", "D'", "E'"],
	"z'": ["F", "S", "B'"]
	}

	middles = {
	#key - wide move, value - normal moves that generates wide move
		"Rw2": ["R2", 'M2'],
		"Uw2": ["U2", 'E2'],
		"Fw2": ["F2", 'S2'],
		"Rw'": ["R'", 'M'],
		"Uw'": ["U'", 'E'],
		"Fw'": ["F'", "S'"],
		"Rw": ["R", "M'"],
		"Uw": ["U", "E'"],
		"Fw": ["F", 'S']
		}
	

	def __init__(self):
		self.rotations_path = [] #list of rotations made by the middle moves
		self.stickers = { #dict of my letter scheme
		'UF': 'buffer',
		'FU': 'buffer',
		'UL': 'E',
		'LU': 'F',
		'UB': 'A',
		'BU': 'B',
		'UR': 'G',
		'RU': 'H',
		'DF': 'I',
		'FD': 'J',
		'DL': 'M',
		'LD': 'N',
		'DB': 'O',
		'BD': 'P',
		'DR': 'K',
		'RD': 'L',
		'FR': 'R',
		'RF': 'S',
		'FL': 'T',
		'LF': 'U',
		'BL': 'W',
		'LB': 'C',
		'BR': 'D',
		'RB': 'Z',
		'UFR': 'buffer',
		'FUR': 'buffer',
		'RUF': 'buffer',
		'UBR': 'A',
		'BUR': 'B',
		'RUB': 'C',
		'UBL': 'D',
		'BUL': 'E',
		'LUB': 'F',
		'UFL': 'G',
		'FUL': 'H',
		'LUF': 'I',
		'DBR': 'J',
		'BDR': 'K',
		'RDB': 'M',
		'DFR': 'N',
		'FDR': 'O',
		'RDF': 'P',
		'DFL': 'R',
		'FDL': 'S',
		'LDF': 'T',
		'DBL': 'U',
		'BDL': 'W',
		'LDB': 'Z'
		}
		
		self.group_by_type()
		

	#groups all targets by the orientated target, eg. value UBL, key UBL BUL LUB
	def group_by_type(self):
		self.groups = {}
		edges, corners = [], []
		for target in self.stickers:
			if len(target) == 2: edges.append(target)
			else: corners.append(target)
		to_add = []
		for n in range(len(edges)):
			to_add.append(edges[n])
			if n%2 == 1:
				self.groups[edges[n-1]] = to_add
				to_add = []

		for n in range(len(corners)):
			to_add.append(corners[n])
			if n%3 == 2:
				self.groups[corners[n-2]] = to_add
				to_add = []

	#converts path of wide moves to the path of rotations
	def assign_rotation(self, move):
		if move[0] in Cube.rotations:
			if len(move) == 1:
				self.rotations_path.append(Cube.rotations[move[0]])
			else:
				self.rotations_path.append(Cube.rotations[move[0]] + move[-1])

	#generates moves leading to white green orientation
	def return_to_WG(self):
		for rot in reversed(self.rotations_path):
			for i in range(3):
				self.returning_moves.append(Cube.rotations[rot][i])


	def scrambling(self, scramble, ring):
		self.raw_scramble = scramble.split() #raw_scramble is a list of normal moves
		self.edited_scramble, self.returning_moves = [], []
		#edited_scramble - raw_scramble + wide moves converted to normal + return to white green

		for move in self.raw_scramble:
			if move.find('w') == -1: self.edited_scramble.append(move)
			else: 
				mvs = Cube.middles[move]
				self.edited_scramble.append(mvs[0])
				self.edited_scramble.append(mvs[1])

		for move in self.edited_scramble:
			self.assign_rotation(move)

		self.return_to_WG()

		self.edited_scramble += self.returning_moves

		for move in self.edited_scramble:
			current_move = Move(move, ring)
			all_cycles = current_move.do()
			#loop changes the letter scheme position after move, eg. before: UB = A, after: UB = E
			for cycles in all_cycles:

				new_stickers = []
				for target in cycles[1]:
					new_stickers.append(self.stickers[target])

				for i in range(4):
					self.stickers[cycles[0][i]] = new_stickers[i]
		




		


		

	