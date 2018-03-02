from DFS import DFS
import time

def main():
	nums = [19, 2, 3, 4, 5, 6]
	dfs = DFS(6, nums, 400, True)
	start = time.time()
	all_solutions = dfs.get_solutions()
	end = time.time()
	for solution in all_solutions:
		print(solution)
	print(end - start)

if __name__ == "__main__":
    main()