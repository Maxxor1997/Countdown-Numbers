#file -- Analysis.py --

from DFS import DFS
from DFS_hash import DFS_hash
import time
import collections
import operator

class Analysis:

	def __init__(self):
		return

	def get_rand_nums(self, n, k):
		return

	def format_all_solutions(self, all_solutions, k, n):
		for sol in all_solutions:
			all_solutions[sol] = 100.0 * all_solutions[sol] / (k**n)
		return all_solutions

	def sort_by_key(self, dict):
		ordered_solutions = sorted(dict.items(), key=operator.itemgetter(0))
		return ordered_solutions

	def sort_by_value(self, dict):
		ordered_solutions = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
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
		return self.sort_by_value(self.format_all_solutions(all_solutions, k, 5))






