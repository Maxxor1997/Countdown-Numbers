#file -- DFS_marked.py --

#generalized countdown problem with the 4 standard operators
class DFS_marked:

	def __init__(self, n, nums):
		self.n = n
		self.nums = nums
		self.all_targets_reachable = set()

	def recursion(self, nums):
		if len(nums) == 1:
			return
		else:
			for i in range(0, len(nums)):
				for j in range(i+1, len(nums)):
					firstNum = nums[i]
					secondNum = nums[j]

					newNum1 = firstNum + secondNum		
					self.all_targets_reachable.add(newNum1)
					newList1 = nums[:]
					newList1.remove(firstNum)
					newList1.remove(secondNum)
					newList1.append(newNum1)
					self.recursion(newList1)

					if firstNum > secondNum:
						newNum2 = firstNum - secondNum
					else:
						newNum2 = secondNum - firstNum
					self.all_targets_reachable.add(newNum2)
					newList2 = nums[:]
					newList2.remove(firstNum)
					newList2.remove(secondNum)
					newList2.append(newNum2)
					self.recursion(newList2)

					newNum3 = firstNum * secondNum
					self.all_targets_reachable.add(newNum3)
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					self.recursion(newList3)

					if(secondNum != 0 and firstNum % secondNum == 0):
						newNum4 = firstNum / secondNum
						self.all_targets_reachable.add(newNum4)
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						self.recursion(newList4)

					elif(firstNum !=0 and secondNum % firstNum == 0):
						newNum4 = secondNum / firstNum
						self.all_targets_reachable.add(newNum4)
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						self.recursion(newList4)


	def get_reachable_targets(self):
		for num in self.nums:
			self.all_targets_reachable.add(num)
		self.recursion (self.nums)
		return self.all_targets_reachable
		