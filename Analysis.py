#file -- Analysis.py --

from DFS import DFS
from DFS_hash import DFS_hash
import time
import collections

class Analysis:

	def __init__(self):
		return

	def get_rand_nums(self, n, k):
		return

	def format_all_solutions(self, all_solutions):
		total = 0.0
		for sol in all_solutions:
			total = total + all_solutions[sol]
		for sol in all_solutions:
			all_solutions[sol] = 100.0 * all_solutions[sol] / total 
		ordered_solutions = collections.OrderedDict(sorted(all_solutions.items()))
		return ordered_solutions

	def get_analysis(self, k):
		all_solutions = dict()
		for a in range(0, k):
			for b in range(0, k):
				for c in range(0, k):
					for d in range (0, k):
						for e in range (0, k):
							nums = [a, b, c, d, e]
							dfs_hash = DFS_hash(5, nums, k)
							solutions = dfs_hash.get_reachable_targets()
							for sol in solutions:
								if not sol in all_solutions:
									all_solutions[sol] = 1
								else:
									all_solutions[sol] = all_solutions[sol] + 1
		return self.format_all_solutions(all_solutions)






