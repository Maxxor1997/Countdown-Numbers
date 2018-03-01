#file -- DFS.py --

#generalized countdown problem with the 4 standard operators
class DFS:

	def __init__(self, n, nums, target):
		self.n = n
		self.nums = nums
		self.target = target
		self.allSolutions = list()

	def add(self, a, b):
		return a+b

	def subtract(self, a, b):
		if a > b:
			return a-b
		else:
			return b-a

	def multiply(self, a, b):
		return a*b

	#assume numbers are divisible
	def divide(self, a, b):
		if a > b:
			return a/b
		else:
			return b/a


	def recursion(self, nums, currPath):
		if len(nums) == 1:
			return
		else:
			for i in range(0, len(nums)):
				for j in range(i+1, len(nums)):
					firstNum = nums[i]
					secondNum = nums[j]

					newNum1 = self.add(firstNum, secondNum)
					newPath1 = currPath + "(" + str(firstNum) + " + " + str(secondNum) + ")"
					if newNum1 == self.target:
						self.allSolutions.append(newPath1)
					newList1 = nums[:]
					newList1.remove(firstNum)
					newList1.remove(secondNum)
					newList1.append(newNum1)
					self.recursion(newList1, newPath1)

					newNum2 = self.subtract(firstNum, secondNum)
					newPath2 = currPath + "(" + str(firstNum) + " - " + str(secondNum) + ")"
					if newNum2 == self.target:
						self.allSolutions.append(newPath2)
					newList2 = nums[:]
					newList2.remove(firstNum)
					newList2.remove(secondNum)
					newList2.append(newNum2)
					self.recursion(newList2, newPath2)

					newNum3 = self.multiply(firstNum, secondNum)
					newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
					if newNum3 == self.target:
						self.allSolutions.append(newPath3)
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					self.recursion(newList3, newPath3)


	def getSolutions(self):
		for num in self.nums:
			if num == self.target:
				self.allSolutions.append(str(num))

		currPath = ""
		solution = self.recursion (self.nums, currPath)
		return self.allSolutions
		