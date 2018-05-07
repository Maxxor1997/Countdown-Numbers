from DFS import DFS
from DFS_marked import DFS_marked
from DFS_hash import DFS_hash
import time
import collections
import operator
import matplotlib.pyplot as plt
import math
from math import log


def sort_and_remove(file, trials, timeout):
	groups = ["Brute Force", "Heuristic 1", "Heuristic 2","Heuristic 3","Heuristic 4","Heuristic 4, adj","Heuristic 5","Heuristic 5, adj"]
	colors = ["black", "red", "green", "blue", "brown", "magenta", "purple", "orange"]
	data = list()
	f = open(file,'r')
	f.readline()
	for k in range(8):
		new_data = list()
		print("iteration: " + str(k))
		f.readline()
		num1 = list()
		for i in range(trials):
			text = f.readline()
			print(text)
			num1.append(float(text))
			num1 = sorted(num1)
		x = 0
		for j in num1:
			if j<timeout:
				new_data.append((x, j))
			x = x+1
		data.append(new_data)

	fig, ax = plt.subplots()

	for i in range(len(data)):
		dat = data[i]
		xs = list(zip(*dat))[0]
		ys = list(zip(*dat))[1]
		ax.scatter(xs, ys, alpha=0.8, c=colors[i], edgecolors='none', s=30, label=groups[i])

	plt.title('Time vs Number of Instances Solved, max target = k^3')
	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels)
	plt.xlabel("Instances Solved")
	plt.ylabel("Time in Seconds")
	plt.show()


    

if __name__ == "__main__":
    # targets1 = use_DFS_hash()
    # targets2 = use_DFS_marked()
    # if len(targets1) != len(targets2):
    # 	print ("discrepancy")
    # for i in range (0, len(targets1)):
    # 	if targets1[i] != targets2[i]:
    # 		print ("discrepancy" + str(targets1[i]))
    sort_and_remove("test_suites_4.txt", 50, 100)