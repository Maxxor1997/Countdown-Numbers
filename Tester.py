from Solver import Solver
from Solver_heuristic import Solver_heuristic
from Solver_heuristic2 import Solver_heuristic2
from DFS import DFS
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

	def gen_target_nums(self, max_target, trials):
		target_numbers = list()
		for i in range(trials):
			target_numbers.append(random.randint(1, max_target))
		return target_numbers

	def base_trials(self, trials, test_cases, target_numbers, debug):
		solved = 0
		off = 0
		time_solved = 0
		time_unsolved = 0
		for i in range(trials):
			if i%(trials/20)==0:
				print(str(i*100/trials) + "%")
			start = time.clock()
			nums = test_cases[i]
			target = target_numbers[i]
			dfs = DFS(len(nums), nums, target, True)
			(closest, solution) = dfs.get_solutions()
			elapsed = time.clock() - start
			if closest == target:
				time_solved = time_solved + elapsed
				solved = solved + 1
			else:
				time_unsolved = time_unsolved + elapsed
				off = off + abs(target - closest)
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(time_solved + time_unsolved))
		if solved==0:
			print("Average Time for Solved Case: " + str(0))
		else:
			print("Average Time for Solved Case: " + str(time_solved/solved))
		if trials-solved==0:
			print("Average Time for Unsolved Case: " + str(0))
		else:
			print("Average Time for Unsolved Case: " + str(time_unsolved/(trials - solved)))

	def brute_force_trials(self, trials, timeout, test_cases, target_numbers, debug):
		solved = 0
		off = 0
		time_solved = 0
		time_unsolved = 0
		print("Starting Brute Force Trials")
		for i in range(trials):
			start = time.clock()
			nums = test_cases[i]
			if debug:
				print(nums)
			target = target_numbers[i]
			if debug:
				print("Target: " + str(target))
			solver = Solver(self.n, target, nums, timeout, debug)
			(closest, solution) = solver.brute_force()
			elapsed = time.clock() - start
			if (closest == target):
				time_solved = time_solved + elapsed
				solved = solved + 1
			else:
				time_unsolved = time_unsolved + elapsed
				off = off + abs(closest - target)
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")
			
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(time_solved + time_unsolved))
		if solved==0:
			print("Average Time for Solved Case: " + str(0))
		else:
			print("Average Time for Solved Case: " + str(time_solved/solved))
		if trials-solved==0:
			print("Average Time for Unsolved Case: " + str(0))
		else:
			print("Average Time for Unsolved Case: " + str(time_unsolved/(trials - solved)))


	def heuristic_trials(self, trials, timeout, test_cases, offset, target_numbers, debug):

		solved = 0
		off = 0
		found_total = 0
		time_solved = 0
		time_unsolved = 0
		print("Starting Heuristic Trials with Offset " + str(offset))
		for i in range(trials):
			start = time.clock()
			nums = test_cases[i]
			if debug:
				print(nums)
			target = target_numbers[i]
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 200, 0.9, debug)
			(closest, solution, found_size) = solver.heuristic_search()
			found_total = found_total + found_size
			elapsed = time.clock() - start
			if (closest == target):
				solved = solved + 1
				time_solved = time_solved + elapsed
			else:
				off = off + abs(closest - target)
				time_unsolved = time_unsolved + elapsed
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")
		
		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Average Found Size: " + str(found_total/trials))
		print("Total Time: " + str(time_solved + time_unsolved))
		if solved==0:
			print("Average Time for Solved Case: " + str(0))
		else:
			print("Average Time for Solved Case: " + str(time_solved/solved))
		if trials-solved==0:
			print("Average Time for Unsolved Case: " + str(0))
		else:
			print("Average Time for Unsolved Case: " + str(time_unsolved/(trials - solved)))


	def heuristic2_trials(self, trials, timeout, test_cases, offset, target_numbers, multiply, debug):
	
		solved = 0
		off = 0
		time_solved = 0
		time_unsolved = 0
		if multiply:
			print("Starting Heuristic 2 Trials with Multiply and Offset " + str(offset))
		else:
			print("Starting Heuristic 2 Trials with Addition and Offset " + str(offset))
		for i in range(trials):
			start = time.clock()
			nums = test_cases[i]
			if debug:
				print(nums)
			target = target_numbers[i]
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic2(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 10, multiply, debug)
			(closest, solution) = solver.heuristic_search_2()
			elapsed = time.clock() - start
			if (closest == target):
				solved = solved + 1
				time_solved = time_solved + elapsed
			else:
				off = off + abs(closest - target)
				time_unsolved = time_unsolved + elapsed
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")


		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(time_solved + time_unsolved))
		if solved==0:
			print("Average Time for Solved Case: " + str(0))
		else:
			print("Average Time for Solved Case: " + str(time_solved/solved))
		if trials-solved==0:
			print("Average Time for Unsolved Case: " + str(0))
		else:
			print("Average Time for Unsolved Case: " + str(time_unsolved/(trials - solved)))


	def heuristic3_trials(self, trials, timeout, test_cases, offset, target_numbers, multiply, adjust_offset, debug):
		
		solved = 0
		off = 0
		time_solved = 0
		time_unsolved = 0
		if adjust_offset:
			print("Starting Heuristic 3 Trials with Adjusted Offset")
		else:
			print("Starting Heuristic 3 Trials with Offset " + str(offset))
		for i in range(trials):
			start = time.clock()
			nums = test_cases[i]
			if debug:
				print(nums)
			target = target_numbers[i]
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic2(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 1, multiply, debug)
			(closest, solution) = solver.heuristic_search_3(adjust_offset)
			elapsed = time.clock() - start
			if (closest == target):
				solved = solved + 1
				time_solved = time_solved + elapsed
			else:
				off = off + abs(closest - target)
				time_unsolved = time_unsolved + elapsed
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")

		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(time_solved + time_unsolved))
		if solved==0:
			print("Average Time for Solved Case: " + str(0))
		else:
			print("Average Time for Solved Case: " + str(time_solved/solved))
		if trials-solved==0:
			print("Average Time for Unsolved Case: " + str(0))
		else:
			print("Average Time for Unsolved Case: " + str(time_unsolved/(trials - solved)))

	def heuristic4_trials(self, trials, timeout, test_cases, offset, target_numbers, multiply, adjust_offset, debug):
		
		solved = 0
		off = 0
		time_solved = 0
		time_unsolved = 0
		if adjust_offset:
			print("Starting Heuristic 4 Trials with Adjusted Offset")
		else:
			print("Starting Heuristic 4 Trials with Offset " + str(offset))
		for i in range(trials):
			start = time.clock()
			nums = test_cases[i]
			if debug:
				print(nums)
			target = target_numbers[i]
			if debug:
				print("Target: " + str(target))
			solver = Solver_heuristic2(self.n, int(self.n / 2) + offset, self.k, target, nums, timeout, 1, multiply, debug)
			(closest, solution) = solver.heuristic_search_4(adjust_offset)
			elapsed = time.clock() - start
			if (closest == target):
				solved = solved + 1
				time_solved = time_solved + elapsed
			else:
				off = off + abs(closest - target)
				time_unsolved = time_unsolved + elapsed
			if debug:
				print("Closest: " + str(closest) + "( " + str(abs(target - closest)) + " off)")
				print(solution)
				print("")

		print("Percentage Solved: " + str(100 * solved / trials) + "%")
		print("Average Error: " + str(off/trials))
		print("Total Time: " + str(time_solved + time_unsolved))
		if solved==0:
			print("Average Time for Solved Case: " + str(0))
		else:
			print("Average Time for Solved Case: " + str(time_solved/solved))
		if trials-solved==0:
			print("Average Time for Unsolved Case: " + str(0))
		else:
			print("Average Time for Unsolved Case: " + str(time_unsolved/(trials - solved)))


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
			
