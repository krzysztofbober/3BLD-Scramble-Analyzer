from cube_rings import *

class Move:
	def __init__(self, move, ring):
		self.ring = ring
		self.move = move
		self.layer = move[0]
		#direction 1 - clockwise, -1 - counterclockwise, 2 - double move
		if len(move) == 1: self.direction = 1
		elif move[-1] == '2': self.direction = 2
		else: self.direction = -1

	#changes permutations of every ring of designated layer
	def do(self):
		cycled_groups = []
		for group in self.ring.rings[self.layer]:
			if self.direction == 1: cycled = [group[3], group[0], group[1], group[2]]
			elif self.direction == -1: cycled = [group[1], group[2], group[3], group[0]]
			else: cycled = [group[2], group[3], group[0], group[1]]
				
			cycled_groups.append([group, cycled])
			#group - ring before the move, cycled - ring after the move
		return cycled_groups #returns permutated rings
