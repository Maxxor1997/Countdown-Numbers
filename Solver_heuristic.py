import random
import time

class Solver_heuristic:

	def __init__(self, n, k, target, nums, timeout, heuristic_range, time_ratio, debug):
		self.start = time.time()
		self.n = n
		self.nums = nums
		self.target = target
		self.timeout = timeout
		self.time_ratio = time_ratio
		self.start = time.time()
		self.debug = debug
		self.hashes = dict()
		self.searched = set()

		#initialize dict structure
		self.most_likely = set()
		file_name = "results_n" + str(int(n/2)) + "_k" + str(k) + ".txt"
		input_file = open(file_name)
		text = input_file.readlines()[1:heuristic_range + 1]
		for line in text:
			index = line.index(":")
			num = line[:index]
			self.most_likely.add(int(num))

		#(closest, solution, likely)
		self.heuristic_targets = dict()
		first = nums[0]
		for num in self.most_likely:
			self.heuristic_targets[self.target + num] = (first, str(first), num)
			self.heuristic_targets[self.target * num] = (first, str(first), num)
			if (num >= self.target):
				self.heuristic_targets[num - self.target] = (first, str(first), num)
			else:
				self.heuristic_targets[self.target - num] = (first, str(first), num)
			if (self.target != 0 and num % self.target == 0):
				self.heuristic_targets[num / self.target] = (first, str(first), num)
			elif (num != 0 and self.target % num == 0):
				self.heuristic_targets[self.target / num] = (first, str(first), num)


	def get_hash(self, nums):
		sum = 0
		for num in nums:
			if not num in self.hashes:
				self.hashes[num] = random.randint(0, 10000000000000)
			sum = sum + self.hashes[num]
		return sum

	def heuristic_search(self):
		half = int(self.n/2)
		first_half = self.nums[:half+1]
		second_half = self.nums[half+1:]

		self.pre_process(first_half, self.heuristic_targets)

		self.recursion(first_half, "", self.start + self.timeout*self.time_ratio)
		if self.debug:
			for tar in self.heuristic_targets:
				print(tar)
				print(self.heuristic_targets[tar])

		self.found = dict()

		self.pre_process_2(second_half, self.most_likely)
		self.recursion_2(second_half, "", self.start + self.timeout)
		if self.debug:
			for f in self.found:
				print(f)
				print(self.found[f])
		found_size = len(self.found)

		final_closest = self.nums[0]
		final_solution = str(self.nums[0])
		for tar in self.heuristic_targets:
			(closest, solution, likely) = self.heuristic_targets[tar]
			if likely in self.found:
				newNum1 = closest + likely
				if abs(newNum1 - self.target) < abs(final_closest - self.target):
					final_closest = newNum1
					final_solution = solution + " + " + self.found[likely]
				if closest >= likely:
					newNum2 = closest - likely
					if abs(newNum2 - self.target) < abs(final_closest - self.target):
						final_closest = newNum2
						final_solution = solution + " - " + self.found[likely]
				else:
					newNum2 = likely - closest
					if abs(newNum2 - self.target) < abs(final_closest - self.target):
						final_closest = newNum2
						final_solution = self.found[likely] + " - " + solution
				newNum3 = closest * likely
				if abs(newNum3 - self.target) < abs(final_closest - self.target):
					final_closest = newNum3
					final_solution = solution + " * " + self.found[likely]
				if likely != 0 and closest % likely == 0:
					newNum4 = closest/likely
					if abs(newNum4 - self.target) < abs(final_closest - self.target):
						final_closest = newNum4
						final_solution = solution + " / " + self.found[likely]
				elif closest != 0 and likely % closest == 0:
					newNum4 = likely/closest
					if abs(newNum4 - self.target) < abs(final_closest - self.target):
						final_closest = newNum4
						final_solution = self.found[likely] + " / " + solution

		return(final_closest, final_solution, found_size)


	def pre_process(self, nums, targets):
		for tar in targets:
			(closest, solution, likely) = targets[tar]
			for num in nums:
				if abs(num - tar) < abs(closest - tar):
					targets[tar] = (num, str(num), likely)

	def pre_process_2(self, nums, targets):
		for num in nums:
			if num in targets:
				self.found[num] = str(num)

	def recursion_2(self, nums, currPath, timeout):
		if time.time() >= timeout:
			return

		if len(nums) == 1:
			return

		hash = self.get_hash(nums)
		if hash in self.searched:
			return
		else:
			self.searched.add(hash)

		for i in range(0, len(nums)):
			for j in range(i+1, len(nums)):
				firstNum = nums[i]
				secondNum = nums[j]

				newNum1 = firstNum + secondNum
				newPath1 = currPath + "(" + str(firstNum) + " + " + str(secondNum) + ")"
				if newNum1 in self.most_likely:
					self.found[newNum1] = newPath1
				newList1 = nums[:]
				newList1.remove(firstNum)
				newList1.remove(secondNum)
				newList1.append(newNum1)
				self.recursion_2(newList1, newPath1, timeout)

				if time.time()>= timeout:
					return

				if (firstNum != secondNum):
					if firstNum > secondNum:
						newNum2 = firstNum - secondNum
						if newNum2 != secondNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							newPath2 = currPath + "(" + str(firstNum) + " - " + str(secondNum) + ")"
							if newNum2 in self.most_likely:
								self.found[newNum2] = newPath2
							self.recursion_2(newList2, newPath2, timeout)
					else:
						newNum2 = secondNum - firstNum
						if newNum2 != firstNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							newPath2 = currPath + "(" + str(secondNum) + " - " + str(firstNum) + ")"
							if newNum2 in self.most_likely:
								self.found[newNum2] = newPath2
							self.recursion_2(newList2, newPath2, timeout)

				if time.time() >= timeout:
					return

				if (firstNum != 1 and secondNum != 1):
					newNum3 = firstNum * secondNum
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
					if newNum3 in self.most_likely:
						self.found[newNum3] = newPath3
					self.recursion_2(newList3, newPath3, timeout)

				if time.time()>= timeout:
					return

				if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
					newNum4 = firstNum / secondNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(firstNum) + " / " + str(secondNum) + ")"
						if newNum4 in self.most_likely:
							self.found[newNum4] = newPath4
						self.recursion_2(newList4, newPath4, timeout)


				if time.time() >= timeout:
					return

				elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
					newNum4 = secondNum / firstNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(secondNum) + " / " + str(firstNum) + ")"
						if newNum4 in self.most_likely:
							self.found[newNum4] = newPath4
						self.recursion_2(newList4, newPath4, timeout)
					
				if time.time() >= timeout:
					return



	def recursion(self, nums, currPath, timeout):

		if time.time() >= timeout:
			return

		if len(nums) == 1:
			return

		hash = self.get_hash(nums)
		if hash in self.searched:
			return
		else:
			self.searched.add(hash)

		for i in range(0, len(nums)):
			for j in range(i+1, len(nums)):
				firstNum = nums[i]
				secondNum = nums[j]

				newNum1 = firstNum + secondNum
				newPath1 = currPath + "(" + str(firstNum) + " + " + str(secondNum) + ")"
				for tar in self.heuristic_targets:
					(closest, solution, likely) = self.heuristic_targets[tar]
					if abs(newNum1 - tar) < abs(closest - tar):
						self.heuristic_targets[tar] = (newNum1, newPath1, likely)
				newList1 = nums[:]
				newList1.remove(firstNum)
				newList1.remove(secondNum)
				newList1.append(newNum1)
				self.recursion(newList1, newPath1, timeout)

				if time.time()>= timeout:
					return

				if (firstNum != secondNum):
					if firstNum > secondNum:
						newNum2 = firstNum - secondNum
						if newNum2 != secondNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							newPath2 = currPath + "(" + str(firstNum) + " - " + str(secondNum) + ")"
							for tar in self.heuristic_targets:
								(closest, solution, likely) = self.heuristic_targets[tar]
								if abs(newNum2 - tar) < abs(closest - tar):
									self.heuristic_targets[tar] = (newNum2, newPath2, likely)
							self.recursion(newList2, newPath2, timeout)
					else:
						newNum2 = secondNum - firstNum
						if newNum2 != firstNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							newPath2 = currPath + "(" + str(secondNum) + " - " + str(firstNum) + ")"
							for tar in self.heuristic_targets:
								(closest, solution, likely) = self.heuristic_targets[tar]
								if abs(newNum2 - tar) < abs(closest - tar):
									self.heuristic_targets[tar] = (newNum2, newPath2, likely)
							self.recursion(newList2, newPath2, timeout)

				if time.time()>= timeout:
					return

				if (firstNum != 1 and secondNum != 1):
					newNum3 = firstNum * secondNum
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
					for tar in self.heuristic_targets:
						(closest, solution, likely) = self.heuristic_targets[tar]
						if abs(newNum3 - tar) < abs(closest - tar):
							self.heuristic_targets[tar] = (newNum3, newPath3, likely)
					self.recursion(newList3, newPath3, timeout)

				if time.time() >= timeout:
					return

				if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
					newNum4 = firstNum / secondNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(firstNum) + " / " + str(secondNum) + ")"
						for tar in self.heuristic_targets:
							(closest, solution, likely) = self.heuristic_targets[tar]
							if abs(newNum4 - tar) < abs(closest - tar):
								self.heuristic_targets[tar] = (newNum4, newPath4, likely)
						self.recursion(newList4, newPath4, timeout)


				if time.time()>= timeout:
					return

				elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
					newNum4 = secondNum / firstNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(secondNum) + " / " + str(firstNum) + ")"
						for tar in self.heuristic_targets:
							(closest, solution, likely) = self.heuristic_targets[tar]
							if abs(newNum4 - tar) < abs(closest - tar):
								self.heuristic_targets[tar] = (newNum4, newPath4, likely)
						self.recursion(newList4, newPath4, timeout)

					
				if time.time()>= timeout:
					return
