#file -- DFS_marked.py --

import random

#generalized countdown problem with the 4 standard operators
#marks all solutions that are reached, uses hash table for optimization
class DFS_hash:

	def __init__(self, n, nums, k):
		self.n = n
		self.nums = nums
		self.k = k
		self.all_targets_reachable = set()
		self.hashes = dict()
		self.searched = set()

	def get_hash(self, nums):
		sum = 0
		for num in nums:
			if not num in self.hashes:
				self.hashes[num] = random.randint(0, 10000000000000)
			sum = sum + self.hashes[num]
		return sum

	def recursion(self, nums):

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
				self.all_targets_reachable.add(newNum1)
				newList1 = nums[:]
				newList1.remove(firstNum)
				newList1.remove(secondNum)
				newList1.append(newNum1)
				self.recursion(newList1)

				if (firstNum != secondNum):
					if firstNum > secondNum:
						newNum2 = firstNum - secondNum
						if newNum2 != secondNum:
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							self.recursion(newList2)
					else:
						newNum2 = secondNum - firstNum
						if newNum2 != firstNum:
							self.all_targets_reachable.add(newNum2)
							newList2 = nums[:]
							newList2.remove(firstNum)
							newList2.remove(secondNum)
							newList2.append(newNum2)
							self.recursion(newList2)

				if (firstNum != 1 and secondNum != 1):
					newNum3 = firstNum * secondNum
					self.all_targets_reachable.add(newNum3)
					newList3 = nums[:]
					newList3.remove(firstNum)
					newList3.remove(secondNum)
					newList3.append(newNum3)
					self.recursion(newList3)

				if(secondNum != 0 and firstNum % secondNum == 0 and secondNum != 1):
					newNum4 = firstNum / secondNum
					if newNum4 != secondNum:
						self.all_targets_reachable.add(newNum4)
						newList4 = nums[:]
						newList4.remove(firstNum)
						newList4.remove(secondNum)
						newList4.append(newNum4)
						self.recursion(newList4)

				elif(firstNum !=0 and secondNum % firstNum == 0 and firstNum != 1):
					newNum4 = secondNum / firstNum
					if newNum4 != secondNum:
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

		