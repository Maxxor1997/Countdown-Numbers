#file -- DFS.py --

#generalized countdown problem with the 4 standard operators
class DFS:

	def __init__(self, n, nums, target, only_one):
		self.n = n
		self.nums = nums
		self.target = target
		self.only_one = only_one
		self.allSolutions = list()
		self.found = False

	def recursion(self, nums, currPath):
		if self.only_one and self.found:
			return
		if len(nums) == 1:
			return
		else:
			for i in range(0, len(nums)):
				for j in range(i+1, len(nums)):
					firstNum = nums[i]
					secondNum = nums[j]

					newNum1 = firstNum + secondNum
					newPath1 = currPath + "(" + str(firstNum) + " + " + str(secondNum) + ")"
					if newNum1 == self.target:
						self.found = True
						self.allSolutions.append(newPath1)
					newList1 = nums[:]
					newList1.remove(firstNum)
					newList1.remove(secondNum)
					newList1.append(newNum1)
					self.recursion(newList1, newPath1)
					if self.only_one and self.found:
						return

					if firstNum != secondNum:
						if firstNum > secondNum:
							newNum2 = firstNum - secondNum
							if newNum2 == secondNum:
								return
							newPath2 = currPath + "(" + str(firstNum) + " - " + str(secondNum) + ")"
						else:
							newNum2 = secondNum - firstNum
							if newNum2 == firstNum:
								return
							newPath2 = currPath + "(" + str(secondNum) + " - " + str(firstNum) + ")"

						if newNum2 == self.target:
							self.found = True
							self.allSolutions.append(newPath2)
						newList2 = nums[:]
						newList2.remove(firstNum)
						newList2.remove(secondNum)
						newList2.append(newNum2)
						self.recursion(newList2, newPath2)
						if self.only_one and self.found:
							return

					if firstNum != 1 and secondNum != 1:
						newNum3 = firstNum * secondNum
						newPath3 = currPath + "(" + str(firstNum) + " x " + str(secondNum) + ")"
						if newNum3 == self.target:
							self.found = True
							self.allSolutions.append(newPath3)
						newList3 = nums[:]
						newList3.remove(firstNum)
						newList3.remove(secondNum)
						newList3.append(newNum3)
						self.recursion(newList3, newPath3)
						if self.only_one and self.found:
							return

					if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
						newNum4 = firstNum / secondNum
						if newNum4 == secondNum:
							return
						newPath4 = currPath + "(" + str(firstNum) + " / " + str(secondNum) + ")"
						if newNum4 == self.target:
							self.found = True
							self.allSolutions.append(newPath4)
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						self.recursion(newList4, newPath4)
						if self.only_one and self.found:
							return

					elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
						newNum4 = secondNum / firstNum
						if newNum4 == secondNum:
							return
						newPath4 = currPath + "(" + str(secondNum) + " / " + str(firstNum) + ")"
						if newNum4 == self.target:
							self.found = True
							self.allSolutions.append(newPath4)
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						self.recursion(newList4, newPath4)
						if self.only_one and self.found:
							return


	def get_solutions(self):
		for num in self.nums:
			if num == self.target:
				self.allSolutions.append(str(num))

		currPath = ""
		solution = self.recursion (self.nums, currPath)
		return self.allSolutions
		