import random
import time

class Solver_heuristic:

	def __init__(self, n, k, target, nums, timeout, heuristic_range):
		self.n = n
		self.nums = nums
		self.target = target
		self.timeout = timeout
		self.hashes = dict()
		self.searched = set()

		self.diff = float("inf") #for debugging

		#initialize dict structure
		most_likely = set()
		file_name = "results_n" + str(int(n/2)) + "_k" + str(k) + ".txt"
		input_file = open(file_name)
		text = input_file.readlines()[1:heuristic_range + 1]
		for line in text:
			index = line.index(":")
			num = line[:index]
			most_likely.add(int(num))

		self.heuristic_targets = dict()
		for num in most_likely:
			self.heuristic_targets[self.target + num] = num
			self.heuristic_targets[self.target * num] = num
			if (num >= self.target):
				self.heuristic_targets[num - self.target] = num
			else:
				self.heuristic_targets[self.target - num] = num
			if (self.target != 0 and num % self.target == 0):
				self.heuristic_targets[num / self.target] = num
			elif (num != 0 and self.target % num == 0):
				self.heuristic_targets[self.target / num] = num

		for num in self.heuristic_targets:
			print(str(num) + " " + str(self.heuristic_targets[num]))


	def get_hash(self, nums):
		sum = 0
		for num in nums:
			if not num in self.hashes:
				self.hashes[num] = random.randint(0, 10000000000000)
			sum = sum + self.hashes[num]
		return sum

	def heuristic_search(self):
		half = int(n/2)
		first_half = self.nums[:half+1]
		second_half = self.nums[half+1:]
		self.start = time.time()
		self.closest = self.nums[0]
		self.solution = ""
		self.curr_target = self.heuristic_targets.keys()[0]
		self.pre_process()

		self.recursion(self.nums, self.solution, self.heuristic_targets)
		return (self.closest, self.solution)


	def pre_process(self):
		for num in self.nums:
			if abs(num - self.target) < abs(self.closest - self.target):
					self.closest = num
					if (self.closest == self.target):
						self.solution = str(num)


	def recursion(self, nums, currPath, heuristic_targets):

		#for debugging
		if abs(self.closest - self.target) < self.diff:
			self.diff = abs(self.closest - self.target)
			print(self.diff)

		if self.closest == self.target:
			return

		if time.time()-self.start >= self.timeout:
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
				if abs(newNum1 - self.target) < abs(self.closest - self.target):
					self.closest = newNum1
					self.solution = newPath1
				newList1 = nums[:]
				newList1.remove(firstNum)
				newList1.remove(secondNum)
				newList1.append(newNum1)
				self.recursion(newList1, newPath1)

				if self.closest == self.target:
					return

				if time.time()-self.start >= self.timeout:
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
							if abs(newNum2 - self.target) < abs(self.closest - self.target):
								self.closest = newNum2
								self.solution = newPath2
							self.recursion(newList2, newPath2)
					else:
						newNum2 = secondNum - firstNum
						if newNum2 != firstNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							newPath2 = currPath + "(" + str(secondNum) + " - " + str(firstNum) + ")"
							if abs(newNum2 - self.target) < abs(self.closest - self.target):
								self.closest = newNum2
								self.solution = newPath2
							self.recursion(newList2, newPath2)

				if self.closest == self.target:
					return

				if time.time()-self.start >= self.timeout:
					return

				if (firstNum != 1 and secondNum != 1):
					newNum3 = firstNum * secondNum
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
					if abs(newNum3 - self.target) < abs(self.closest - self.target):
						self.closest = newNum3
						self.solution = newPath3
					self.recursion(newList3, newPath3)

				if self.closest == self.target:
					return

				if time.time()-self.start >= self.timeout:
					return

				if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
					newNum4 = firstNum / secondNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(firstNum) + " / " + str(secondNum) + ")"
						if abs(newNum4 - self.target) < abs(self.closest - self.target):
							self.closest = newNum4
							self.solution = newPath4
						self.recursion(newList4, newPath4)

				if self.closest == self.target:
					return

				if time.time()-self.start >= self.timeout:
					return

				elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
					newNum4 = secondNum / firstNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(secondNum) + " / " + str(firstNum) + ")"
						if abs(newNum4 - self.target) < abs(self.closest - self.target):
							self.closest = newNum4
							self.solution = newPath4
						self.recursion(newList4, newPath4)

				if self.closest == self.target:
					return
					
				if time.time()-self.start >= self.timeout:
					return
