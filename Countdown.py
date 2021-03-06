#file -- Countdown.py --

from DFS import DFS
from DFS_marked import DFS_marked
from DFS_hash import DFS_hash
from Analysis import Analysis
from Solver import Solver
from Tester import Tester
import time

def use_DFS():
	nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	dfs = DFS(10, nums, 3.5, False)
	start = time.time()
	all_solutions = dfs.get_solutions()
	end = time.time()
	if len(all_solutions) == 0:
		print ("no solutions were found")
	for solution in all_solutions:
		print(solution)
	print(end - start)

def use_DFS_marked():
	nums = [1, 2, 2, 2, 2]
	dfs_marked = DFS_marked(5, nums, 2)
	start = time.time()
	all_targets_reachable = sorted(dfs_marked.get_reachable_targets())
	for target in all_targets_reachable:
		print(target)
	end = time.time()
	print("no hash " + str(end - start))
	return all_targets_reachable

def use_DFS_hash():
	nums = [1, 2, 32, 2, 19, 2, 5, 2, 2, 2]
	dfs_hash= DFS_hash(10, nums, 100)
	start = time.time()
	all_targets_reachable = sorted(dfs_hash.get_reachable_targets())
	for target in all_targets_reachable[0:100]:
		print(target)
	end = time.time()
	print("with hash " + str(end - start))
	return all_targets_reachable

def use_Analysis(n, k):
    analysis = Analysis()
    start = time.time()
    all_solutions = analysis.get_analysis(n, k)
    end = time.time()
    average = (end - start) / (k**n)
    print("k = " + str(k))
    for (key, value) in all_solutions:
      print(str(key) + ": " + str(value) + "%")
    print("total time: " + str(end - start))
    print("average time: " + str(average))
    analysis.visualize(all_solutions, k)

def test_suite(tester, n, k, t, max_target, trials, debug, test_cases, target_numbers, run_base):

    print("n = " + str(n))
    print("k = " + str(k))
    print("Timeout = " + str(t) + "s")
    print("Max Target is " + str(max_target))
    print("Number of trials: " + str(trials))
    print("")

    #15, 8, 15, 12, 11, 14
    print(" Progress | Algorithm Used | Solved | Average Error | Total Time | Avg Solved | Avg Unsolved")
    print("--------------------------------------------------------------------------------------------")

    if (run_base):
        tester.base_trials(trials, test_cases, target_numbers, debug)
        print("")

    tester.brute_force_trials(trials, t, test_cases, target_numbers, debug)
    tester.heuristic_trials(trials, t, test_cases, 0, target_numbers, debug)
    tester.heuristic2_trials(trials, t, test_cases, 0, target_numbers, True, debug)
    tester.heuristic2_trials(trials, t, test_cases, 0, target_numbers, False, debug)
    tester.heuristic3_trials(trials, t, test_cases, 0, target_numbers, True, False, debug)
    tester.heuristic3_trials(trials, t, test_cases, 1, target_numbers, True, True, debug)
    tester.heuristic4_trials(trials, t, test_cases, 0, target_numbers, True, False, debug)
    tester.heuristic4_trials(trials, t, test_cases, 0, target_numbers, True, True, debug)
    print("")

if __name__ == "__main__":
    # targets1 = use_DFS_hash()
    # targets2 = use_DFS_marked()
    # if len(targets1) != len(targets2):
    # 	print ("discrepancy")
    # for i in range (0, len(targets1)):
    # 	if targets1[i] != targets2[i]:
    # 		print ("discrepancy" + str(targets1[i]))
    n = 10
    k = 25
    t = 5
    max_target = k**3
    trials = 1000
    debug = False

    tester = Tester(n, k)
    test_cases = tester.gen_test_nums(n, k, trials)
    target_numbers = tester.gen_target_nums(max_target, trials)

    timeouts = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    for time in timeouts:
        test_suite(tester, n, k, time, max_target, trials, debug, test_cases, target_numbers, False)

    max_target = k**4
    
    for time in timeouts:
        test_suite(tester, n, k, time, max_target, trials, debug, test_cases, target_numbers, False)


