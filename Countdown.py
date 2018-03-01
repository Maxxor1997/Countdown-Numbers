from DFS import DFS

def main():
	nums = [19, 2, 3, 4, 5, 6]
	dfs = DFS(6, nums, 19)
	allSolutions = dfs.getSolutions()
	for solution in allSolutions:
		print(solution)

if __name__ == "__main__":
    main()