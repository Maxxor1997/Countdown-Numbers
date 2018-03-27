from Solver import Solver
from Solver_heuristic import Solver_heuristic
import time
import random
import math

class Tester:

	def __init__(self, n, k):
		self.n = n
		self.k = k

	def gen_rand_nums(self, n, k):
		nums = list()
		for i in range(n):
			rand = random.randint(1, k)
			nums.append(rand)
		return nums

	def max_possible(self, nums):
		product = 1
		for num in nums:
			product = product * num
		return product

	def brute_force_trials(self, trials, timeout):
		start = time.time()
		solved = 0
		off = 0
		print("Starting Brute Force Trials")
		for i in range(trials):
			nums = self.gen_rand_nums(self.n, self.k)
			print(nums)
			target = random.randint(1, int(math.sqrt(self.max_possible(nums))))
			print("Target: " + str(target))
			solver = Solver(self.n, target, nums, timeout)
			(closest, solution) = solver.brute_force()
			if (closest == target):
				solved = solved + 1
			else:
				off = off + abs(closest - target)
			print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
			print(solution)
		end = time.time()
		average = (end - start) / trials
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(end - start))
		print("Average Time: " + str(average))

	def heuristic_trials(self, trials, timeout):
		start = time.time()
		solved = 0
		off = 0
		print("Starting Heuristic Trials")
		for i in range(trials):
			nums = self.gen_rand_nums(self.n, self.k)
			print(nums)
			target = random.randint(1, int(math.sqrt(self.max_possible(nums))))
			print("Target: " + str(target))
			solver = Solver_heuristic(self.n, self.k, target, nums, timeout, 100)
			(closest, solution) = solver.heuristic_search()
			if (closest == target):
				solved = solved + 1
			else:
				off = off + abs(closest - target)
			print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
			print(solution)
		end = time.time()
		average = (end - start) / trials
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(end - start))
		print("Average Time: " + str(average))

	def heuristic_trials_test(self, trials, timeout):
		start = time.time()
		solved = 0
		off = 0
		print("Starting Heuristic Trials Test")
		nums = self.gen_rand_nums(self.n, self.k)
		target = random.randint(1, int(math.sqrt(self.max_possible(nums))))
		print("Target is " + str(target))
		solver = Solver_heuristic(self.n, self.k, target, nums, timeout, 2)
			
