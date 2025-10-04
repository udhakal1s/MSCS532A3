# Umesh Dhakal
# MSCS532A3
# Randomized and Deterministic Quick Sort Implementation and comparing the results

import random
import time
import tracemalloc
import sys
sys.setrecursionlimit(10000)

# Function for partitioning through pivot
def partition(arraylist, leftindex, rightindex, randompivot=False):
    # choosing the random pivot
    if randompivot:
        pivotpoint = random.randint(leftindex, rightindex)
        arraylist[pivotpoint], arraylist[rightindex] = arraylist[rightindex], arraylist[pivotpoint]
    else:
        # Always chhosing the first element as pivot
        arraylist[leftindex], arraylist[rightindex] = arraylist[rightindex], arraylist[leftindex]
    pivotvalue = arraylist[rightindex]
    a = leftindex - 1
    for b in range(leftindex, rightindex):
        if arraylist[b] <= pivotvalue:
            a += 1
            arraylist[a], arraylist[b] = arraylist[b], arraylist[a]
    arraylist[a + 1], arraylist[rightindex] = arraylist[rightindex], arraylist[a + 1]
    return a + 1

# Recursive function for quicksort
def quicksort(arraylist, leftindex, rightindex, randompivot=False):
    if leftindex < rightindex:
        pivotpoint = partition(arraylist, leftindex, rightindex, randompivot)
        quicksort(arraylist, leftindex, pivotpoint - 1, randompivot)
        quicksort(arraylist, pivotpoint + 1, rightindex, randompivot)

# Run performance test
def run(algorithm, dataset, dataset_name, randompivot=False):
    tracemalloc.start()
    starttime = time.time()
    algorithm(dataset, 0, len(dataset) - 1, randompivot)
    endtime = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    mode = "Randomized" if randompivot else "Deterministic"
    #memroy usage and time taken
    print(f"{mode} Quicksort on {dataset_name} took {endtime-starttime:.5f} seconds with {peak/1024:.2f} KB memory")

# Using differnt datasets like sorted, reverse data, all same repeted data, random data
test_data = 2000
datasets = {
    "Sorted Data": list(range(1, test_data + 1)),
    "Reverse Data": list(range(test_data, 0, -1)),
    "Random Data": [random.randint(1, test_data) for _ in range(test_data)],
    "Repeated Data": [5] * test_data   
}

print("\nQuick Sort Performance Analysis\n")
for dataset_name, dataset in datasets.items():
    # when pivot is random
    run(quicksort, dataset[:], dataset_name, randompivot=True) 
    # when pivot is first element  
    run(quicksort, dataset[:], dataset_name, randompivot=False)  