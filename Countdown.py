#file -- Countdown.py --

from DFS import DFS
from DFS_marked import DFS_marked
import time

def use_DFS():
	nums = [5, 3, 10, 30, 4, 19]
	dfs = DFS(10, nums, 143, True)
	start = time.time()
	all_solutions = dfs.get_solutions()
	end = time.time()
	for solution in all_solutions:
		print(solution)
	print(end - start)

def use_DFS_marked():
	nums = [1, 2, 3, 4, 5]
	dfs_marked = DFS_marked(5, nums)
	start = time.time()
	all_targets_reachable = dfs_marked.get_reachable_targets()
	for target in all_targets_reachable:
		print (target)

if __name__ == "__main__":
    use_DFS_marked()