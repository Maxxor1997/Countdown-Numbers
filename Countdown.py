from DFS import DFS
import time

def main():
	nums = [5, 3, 10, 30, 4, 19]
	dfs = DFS(10, nums, 700, True)
	start = time.time()
	all_solutions = dfs.get_solutions()
	end = time.time()
	for solution in all_solutions:
		print(solution)
	print(end - start)

if __name__ == "__main__":
    main()