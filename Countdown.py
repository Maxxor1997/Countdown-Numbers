#file -- Countdown.py --

from DFS import DFS
from DFS_marked import DFS_marked
from DFS_hash import DFS_hash
from Analysis import Analysis
import time

def use_DFS():
	nums = [7, 2, 19, 4, 5, 6]
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
	nums = [1, 2, 3, 4, 4]
	dfs_marked = DFS_marked(5, nums)
	start = time.time()
	all_targets_reachable = sorted(dfs_marked.get_reachable_targets())
	end = time.time()
	print("no hash " + str(end - start))
	return all_targets_reachable

def use_DFS_hash():
	nums = [1, 2, 3, 4, 4]
	dfs_hash= DFS_hash(5, nums, 100)
	start = time.time()
	all_targets_reachable = sorted(dfs_hash.get_reachable_targets())
	end = time.time()
	print("with hash " + str(end - start))
	return all_targets_reachable

if __name__ == "__main__":
    # targets1 = use_DFS_hash()
    # targets2 = use_DFS_marked()
    # if len(targets1) != len(targets2):
    # 	print ("discrepancy")
    # for i in range (0, len(targets1)):
    # 	if targets1[i] != targets2[i]:
    # 		print ("discrepancy" + str(targets1[i]))
    k = 10
    analysis = Analysis()
    start = time.time()
    all_solutions = analysis.get_analysis(k)
    end = time.time()
    average = (end - start) / (k**5)
    for (key, value) in all_solutions:
    	print(str(key) + ": " + str(value) + "%")
    print("total time: " + str(end - start))
    print("average time: " + str(average))
