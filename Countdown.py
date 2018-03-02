from DFS import DFS
import time

def main():
	nums = [19, 2, 3, 4, 5, 6]
	dfs = DFS(6, nums, 200)
	start = time.time()
	allSolutions = dfs.getSolutions()
	end = time.time()
	for solution in allSolutions:
		print(solution)
	print(end - start)

if __name__ == "__main__":
    main()