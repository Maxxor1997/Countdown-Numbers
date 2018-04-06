from Solver import Solver
from Solver_heuristic import Solver_heuristic
from Solver_heuristic2 import Solver_heuristic2
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

	def gen_test_nums(self, n, k, trials):
		test_cases = list()
		for i in range(trials):
			test_cases.append(self.gen_rand_nums(n, k))
		return test_cases

	def brute_force_trials(self, trials, timeout, test_cases, max_target, debug):
		start = time.clock()
		solved = 0
		off = 0
		print("Starting Brute Force Trials")
		for i in range(trials):
			nums = test_cases[i]
			if debug:
				print(nums)
			target = random.randint(1, max_target)
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
				print("")
		end = time.clock()
		average = (end - start) / trials
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(end - start))
		print("Average Time: " + str(average))

	def heuristic_trials(self, trials, timeout, test_cases, offset, max_target, debug):
		start = time.clock()
		solved = 0
		off = 0
		found_total = 0
		print("Starting Heuristic Trials with Offset " + str(offset))
		for i in range(trials):
			nums = test_cases[i]
			if debug:
				print(nums)
			target = random.randint(1, max_target)
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

	def heuristic2_trials(self, trials, timeout, test_cases, offset, max_target, multiply, debug):
		start = time.clock()
		solved = 0
		off = 0
		if multiply:
			print("Starting Heuristic 2 Trials with Multiply and Offset " + str(offset))
		else:
			print("Starting Heuristic 2 Trials with Addition and Offset " + str(offset))
		for i in range(trials):
			nums = test_cases[i]
			if debug:
				print(nums)
			target = random.randint(1, max_target)
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic2(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 10, multiply, debug)
			(closest, solution) = solver.heuristic_search_2()
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
		print("Total Time: " + str(end - start))
		print("Average Time: " + str(average))

	def heuristic3_trials(self, trials, timeout, test_cases, offset, max_target, multiply, debug):
		start = time.clock()
		solved = 0
		off = 0
		if multiply:
			print("Starting Heuristic 3 Trials with Offset " + str(offset))
		else:
			print("Starting Heuristic 2 Trials with Offset " + str(offset))
		for i in range(trials):
			nums = test_cases[i]
			if debug:
				print(nums)
			target = random.randint(1, max_target)
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic2(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 1, multiply, debug)
			(closest, solution) = solver.heuristic_search_3()
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
		end = time.clock()
		print("Time elapsed: " + str(end - start))
			
