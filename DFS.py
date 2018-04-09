#file -- DFS.py --

#generalized countdown problem with the 4 standard operators
#returns as soon as one solution is found
import random

class DFS:

	def __init__(self, n, nums, target, only_one):
		self.n = n
		self.nums = nums
		self.target = target
		self.closest = 0
		self.solution = ""
		self.hashes = dict()
		self.searched = set()

	def get_hash(self, nums):
		sum = 0
		for num in nums:
			if not num in self.hashes:
				self.hashes[num] = random.randint(0, 10000000000000)
			sum = sum + self.hashes[num]
		return sum

	def recursion(self, nums, currPath):
		if self.closest == self.target:
			return

		hash = self.get_hash(nums)
		if hash in self.searched:
			return
		else:
			self.searched.add(hash)

		if len(nums) == 1:
			return
		else:
			for i in range(0, len(nums)):
				for j in range(i+1, len(nums)):
					firstNum = nums[i]
					secondNum = nums[j]

					newNum1 = firstNum + secondNum
					newPath1 = currPath + "(" + str(firstNum) + " + " + str(secondNum) + ")"
					if abs(newNum1 - self.target) < abs(self.target - self.closest):
						self.closest = newNum1
						self.solution = newPath1
					newList1 = nums[:]
					newList1.remove(firstNum)
					newList1.remove(secondNum)
					newList1.append(newNum1)
					self.recursion(newList1, newPath1)
					if self.closest == self.target:
						return

					if firstNum != secondNum:
						if firstNum > secondNum:
							newNum2 = firstNum - secondNum
							if newNum2 != secondNum:
								newPath2 = currPath + "(" + str(firstNum) + " - " + str(secondNum) + ")"
								if abs(newNum2 - self.target) < abs(self.target - self.closest):
									self.closest = newNum2
									self.solution = newPath2
								newList2 = nums[:]
								newList2.remove(firstNum)
								newList2.remove(secondNum)
								newList2.append(newNum2)
								self.recursion(newList2, newPath2)
								if self.closest == self.target:
									return
						else:
							newNum2 = secondNum - firstNum
							if newNum2 != firstNum:
								newPath2 = currPath + "(" + str(secondNum) + " - " + str(firstNum) + ")"
								if abs(newNum2 - self.target) < abs(self.target - self.closest):
									self.closest = newNum2
									self.solution = newPath2
								newList2 = nums[:]
								newList2.remove(firstNum)
								newList2.remove(secondNum)
								newList2.append(newNum2)
								self.recursion(newList2, newPath2)
								if self.closest == self.target:
									return


					if firstNum != 1 and secondNum != 1:
						newNum3 = firstNum * secondNum
						newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
						if abs(newNum3 - self.target) < abs(self.target - self.closest):
							self.closest = newNum3
							self.solution = newPath3
						newList3 = nums[:]
						newList3.remove(firstNum)
						newList3.remove(secondNum)
						newList3.append(newNum3)
						self.recursion(newList3, newPath3)
						if self.closest == self.target:
							return

					if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
						newNum4 = firstNum / secondNum
						if newNum4 != secondNum:
							newPath4 = currPath + "(" + str(firstNum) + " / " + str(secondNum) + ")"
							if abs(newNum4 - self.target) < abs(self.target - self.closest):
								self.closest = newNum4
								self.solution = newPath4
							newList4 = nums[:]
							newList4.remove(firstNum)
							newList4.remove(secondNum)
							newList4.append(newNum4)
							self.recursion(newList4, newPath4)
							if self.closest == self.target:
								return

					elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
						newNum4 = secondNum / firstNum
						if newNum4 != secondNum:
							newPath4 = currPath + "(" + str(secondNum) + " / " + str(firstNum) + ")"
							if abs(newNum4 - self.target) < abs(self.target - self.closest):
								self.closest = newNum4
								self.solution = newPath4
							newList4 = nums[:]
							newList4.remove(firstNum)
							newList4.remove(secondNum)
							newList4.append(newNum4)
							self.recursion(newList4, newPath4)
							if self.closest == self.target:
								return

	def get_solutions(self):
		for num in self.nums:
			if abs(num - self.target) < abs(self.target - self.closest):
					self.closest = num
					self.solution = str(num)
		currPath = ""
		self.recursion (self.nums, currPath)
		return (self.closest, self.solution)
		