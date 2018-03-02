#file -- Countdown.py --

from DFS import DFS
from DFS_marked import DFS_marked
from DFS_hash import DFS_hash
import time

def use_DFS():
	nums = [1, 2, 3, 4, 5]
	dfs = DFS(5, nums, 1, False)
	start = time.time()
	all_solutions = dfs.get_solutions()
	end = time.time()
	if len(all_solutions) == 0:
		print ("no solutions were found")
	for solution in all_solutions:
		print(solution)
	print(end - start)

def use_DFS_marked():
	nums = [1, 2, 3, 4, 5]
	dfs_marked = DFS_marked(5, nums)
	start = time.time()
	all_targets_reachable = dfs_marked.get_reachable_targets()
	end = time.time()
	for target in all_targets_reachable:
		print (target)
	print(end - start)

def use_DFS_hash():
	nums = [1, 2, 3, 4, 5]
	dfs_hash= DFS_hash(5, nums, 20)
	start = time.time()
	all_targets_reachable = dfs_hash.get_reachable_targets()
	end = time.time()
	for target in all_targets_reachable:
		print (target)
	print(end - start)

if __name__ == "__main__":
    use_DFS_marked()