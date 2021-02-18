class Ring:
	def __init__(self):
		#key - move, value - cycle of permutated targets by the move
		self.rings = {
				'U': [['UF', 'UL', 'UB', 'UR'], ['FU', 'LU', 'BU', 'RU'], 
				['UFR', 'UFL', 'UBL', 'UBR'], ['FUR', 'LUF', 'BUL', 'RUB'], ['RUF', 'FUL', 'LUB', 'BUR']],
				'D': [['DF', 'DR', 'DB', 'DL'], ['FD', 'RD', 'BD', 'LD'],
				['DFR', 'DBR', 'DBL', 'DFL'], ['FDR', 'RDB', 'BDL', 'LDF'], ['RDF', 'BDR', 'LDB', 'FDL']],
				'R': [['UR', 'BR', 'DR', 'FR'], ['RU', 'RB', 'RD', 'RF'], 
				['UFR', 'BUR', 'DBR', 'FDR'], ['FUR', 'UBR', 'BDR', 'DFR'], ['RUF', 'RUB', 'RDB', 'RDF']],
				'L': [['UL', 'FL', 'DL', 'BL'], ['LU', 'LF', 'LD', 'LB'], 
				['UFL', 'FDL', 'DBL', 'BUL'], ['FUL', 'DFL', 'BDL', 'UBL'], ['LUF', 'LDF', 'LDB', 'LUB']],
				'F': [['UF', 'RF', 'DF', 'LF'], ['FU', 'FR', 'FD', 'FL'], 
				['UFR', 'RDF', 'DFL', 'LUF'], ['FUR', 'FDR', 'FDL', 'FUL'], ['RUF', 'DFR', 'LDF', 'UFL']],
				'B': [['UB', 'LB', 'DB', 'RB'], ['BU', 'BL', 'BD', 'BR'], 
				['UBR', 'LUB', 'DBL', 'RDB'], ['BUR', 'BUL', 'BDL', 'BDR'], ['RUB', 'UBL', 'LDB', 'DBR']],
				'M': [['UF', 'FD', 'DB', 'BU'], ['FU', 'DF', 'BD', 'UB']],
				'S': [['UR', 'RD', 'DL', 'LU'], ['RU', 'DR', 'LD', 'UL']],
				'E': [['FL', 'RF', 'BR', 'LB'], ['LF', 'FR', 'RB', 'BL']]
				}
	
	#finally unused method generates missing rings
	'''
	def permutations(self):

		for r in self.rings:
			perms = []
			for group in self.rings[r]:
				if len(group) == 0: continue
				p = []
				if len(group[0]) == 2:
					for target in group:
						p.append(target[1] + target[0])
					perms.append(p)
				else:
					n = 0
					for _ in range(2):
						for target in group:
							if n%2 == 0: p.append(Ring.corectness(target[1] + target[0] + target[2]))
							else: p.append(Ring.corectness(target[2] + target[0] + target[1]))
							n = n+1
						
						n = n+1
					
					perms.append(p[0:4])
					perms.append(p[4:])
					print(r,perms)
			all_targets = self.rings[r] + perms
			self.rings[r] = all_targets
	
	@staticmethod
	def corectness(target):
		if target[0] == 'U' or target[0] == 'D': 
			print(target)
			if target[1] == 'B' or target[1] == 'F': return target
			else: 
				target = target[0] + target[2] + target[1]
				return target
		else:
			if target[1] == 'U' or target[1] == 'D': return target
			else: 
				target = target[0] + target[2] + target[1]
				return target
				'''