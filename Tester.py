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

	def brute_force_trials(self, trials, timeout, debug):
		start = time.clock()
		solved = 0
		off = 0
		print("Starting Brute Force Trials")
		for i in range(trials):
			nums = self.gen_rand_nums(self.n, self.k)
			if debug:
				print(nums)
			target = random.randint(1, int(math.sqrt(self.max_possible(nums))))
			if debug:
				print("Target: " + str(target))
			solver = Solver(self.n, target, nums, timeout, debug)
			(closest, solution) = solver.brute_force()
			if (closest == target):
				solved = solved + 1
			else:
				off = off + abs(closest - target)
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
		end = time.clock()
		average = (end - start) / trials
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(end - start))
		print("Average Time: " + str(average))

	def heuristic_trials(self, trials, timeout, offset, debug):
		start = time.clock()
		solved = 0
		off = 0
		found_total = 0
		print("Starting Heuristic Trials")
		for i in range(trials):
			nums = self.gen_rand_nums(self.n, self.k)
			if debug:
				print(nums)
			target = random.randint(1, int(math.sqrt(self.max_possible(nums))))
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 200, 0.9, debug)
			(closest, solution, found_size) = solver.heuristic_search()
			found_total = found_total + found_size
			if (closest == target):
				solved = solved + 1
			else:
				off = off + abs(closest - target)
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")
		end = time.clock()
		average = (end - start) / trials
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Average Found Size: " + str(found_total/trials))
		print("Total Time: " + str(end - start))
		print("Average Time: " + str(average))

	def heuristic_trials_test(self, trials, timeout):
		start = time.clock()
		solved = 0
		off = 0
		print("Starting Heuristic Trials Test")
		nums = self.gen_rand_nums(self.n, self.k)
		target = random.randint(1, int(math.sqrt(self.max_possible(nums))))
		solver = Solver_heuristic(self.n, self.k, target, nums, timeout, 300)
		(closest, solution) = solver.heuristic_search()
		print("Target is " + str(target))
		print("Closest: " + str(closest))
		print("Solution: " + str(solution))
		end = time.time()
		print("Time elapsed: " + str(end - start))
			
