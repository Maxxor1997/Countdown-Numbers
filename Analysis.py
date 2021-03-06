#file -- Analysis.py --

from DFS import DFS
from DFS_marked import DFS_marked
from DFS_hash import DFS_hash
import time
import collections
import operator
import matplotlib.pyplot as plt
import math
from math import log

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

	def visualize(self, ordered_solutions, k):
		lst = [(elem1, elem2) for elem1, elem2 in ordered_solutions]
		plt.scatter(*zip(*lst))
		plt.xlabel("Target Number")
		plt.ylabel("Probability of Having a Solution")
		plt.title("k = " + str(k))
		plt.show()

	def get_scaling_factor(self, nums):
		scaling = math.factorial(len(nums))
		duplicates = list()
		curr_num = nums[0]
		count = 0
		for num in nums:
			if num == curr_num:
				count = count + 1
			else:
				duplicates.append(count)
				curr_num = num
				count = 1
		duplicates.append(count)
		for dup in duplicates:
			scaling = scaling / math.factorial(dup)
		return scaling


	def get_analysis(self, n, k):
		if n == 4:
			return self.get_analysis_4(k)
		elif n == 5:
			return self.get_analysis_5(k)
		else:
		 	return None

	def get_analysis_5(self, k):
		all_solutions = dict()
		for a in range(1, k+1):
			print(a)
			for b in range(a, k+1):
				for c in range(b, k+1):
					for d in range (c, k+1):
						for e in range (d, k+1):
							nums = [a, b, c, d, e]
							dfs_hash = DFS_hash(5, nums, k)
							solutions = dfs_hash.get_reachable_targets()
							scaling_factor = self.get_scaling_factor(nums)
							for sol in solutions:
								if not sol in all_solutions:
									all_solutions[sol] = scaling_factor
								else:
									all_solutions[sol] = all_solutions[sol] + scaling_factor
		return self.sort_by_value(self.format_all_solutions(all_solutions, k, 5))

	def get_analysis_4(self, k):
		all_solutions = dict()
		for a in range(1, k+1):
			for b in range(a, k+1):
				for c in range(b, k+1):
					for d in range (c, k+1):
						nums = [a, b, c, d]
						dfs_hash = DFS_hash(4, nums, k)
						solutions = dfs_hash.get_reachable_targets()
						scaling_factor = self.get_scaling_factor(nums)
						for sol in solutions:
							if not sol in all_solutions:
								all_solutions[sol] = scaling_factor
							else:
								all_solutions[sol] = all_solutions[sol] + scaling_factor
		return self.sort_by_value(self.format_all_solutions(all_solutions, k, 4))





