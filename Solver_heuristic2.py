import random
import time

class Solver_heuristic2:
	

	def __init__(self, n, first_half, k, target, nums, timeout, num_searches, debug):
		self.n = n
		self.nums = nums
		self.target = target
		self.timeout = timeout
		self.first_half = first_half
		self.num_searches = num_searches
		self.start = time.clock()
		self.debug = debug
		self.hashes = dict()

	def get_hash(self, nums):
		sum = 0
		for num in nums:
			if not num in self.hashes:
				self.hashes[num] = random.randint(0, 10000000000000)
			sum = sum + self.hashes[num]
		return sum

	def shuffle_nums(self, nums):
		return random.shuffle(nums)

	def pre_process_2(self, nums):
		for num in nums:
			if abs(num - self.curr_target)<abs(self.closest - self.curr_target):
				self.closest = num
				self.solution = str(num)

	def heuristic_search_2(self):
		if self.target % 2 == 0:
			first_target = self.target/2
			second_target = first_target
		else:
			first_target = (self.target - 1)/2
			second_target = first_target + 1

		nearest = 0
		solution = ""

		while time.clock() <= self.start + self.timeout:
			shuffled_nums = self.shuffle_nums(self.nums)
			first_half = shuffled_nums[:self.first_half]
			second_half = shuffled_nums[self.first_half:]

			#search first half
			self.nearest = 0
			self.solution = ""
			self.curr_target = first_target
			self.pre_process_2(first_half)
			recursion(first_half, "", self.timeout/(2 * self.num_searches))
			nearest_first = self.nearest
			solution_first = self.solution

			#search second half
			self.nearest = 0
			self.solution = ""
			self.curr_target = second_target
			self.pre_process_2(second_half)
			recursion(second_half, "", self.timeout/(2 * self.num_searches))
			nearest_second = self.nearest
			solution_second = self.solution

			#combine and update
			nearest_total = nearest_first + nearest_second
			solution_total = solution_first + " + " + solution_second
			if abs(nearest_total - self.target) < abs(nearest - self.target):
				nearest = nearest_total
				solution = solution_total
			if nearest == self.target:
				return(nearest, solution)

		return(nearest, solution)


	def recursion(self, nums, currPath, timeout):
		if time.clock() >= timeout || self.curr_target == self.closest:
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
				if abs(newNum1 - self.curr_target) < abs(self.closest - self.curr_target):
					self.closest = newNum1
					self.solution = newPath1
				newList1 = nums[:]
				newList1.remove(firstNum)
				newList1.remove(secondNum)
				newList1.append(newNum1)
				self.recursion(newList1, newPath1, timeout)

				if time.clock()>= timeout || self.curr_target == self.closest:
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
							if abs(newNum2 - self.curr_target) < abs(self.closest - self.curr_target):
								self.closest = newNum2
								self.solution = newPath2
							self.recursion(newList2, newPath2, timeout)
					else:
						newNum2 = secondNum - firstNum
						if newNum2 != firstNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							newPath2 = currPath + "(" + str(secondNum) + " - " + str(firstNum) + ")"
							if abs(newNum2 - self.curr_target) < abs(self.closest - self.curr_target):
								self.closest = newNum2
								self.solution = newPath2
							self.recursion(newList2, newPath2, timeout)

				if time.clock()>= timeout || self.curr_target == self.closest:
					return

				if (firstNum != 1 and secondNum != 1):
					newNum3 = firstNum * secondNum
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
					if abs(newNum3 - self.curr_target) < abs(self.closest - self.curr_target):
						self.closest = newNum3
						self.solution = newPath3
					self.recursion(newList3, newPath3, timeout)

				if time.clock() >= timeout || self.curr_target == self.closest:
					return

				if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
					newNum4 = firstNum / secondNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(firstNum) + " / " + str(secondNum) + ")"
						if abs(newNum4 - self.curr_target) < abs(self.closest - self.curr_target):
							self.closest = newNum4
							self.solution = newPath4
						self.recursion(newList4, newPath4, timeout)


				if time.clock()>= timeout || self.curr_target == self.closest:
					return

				elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
					newNum4 = secondNum / firstNum
					if newNum4 != secondNum:
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						newPath4 = currPath + "(" + str(secondNum) + " / " + str(firstNum) + ")"
						if abs(newNum4 - self.curr_target) < abs(self.closest - self.curr_target):
							self.closest = newNum4
							self.solution = newPath4
						self.recursion(newList4, newPath4, timeout)

					
				if time.clock()>= timeout || self.curr_target == self.closest:
					return