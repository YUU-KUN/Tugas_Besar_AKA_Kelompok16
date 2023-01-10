import random
import time

def bubble_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.time()
    print("Bubble sort time: ", end_time - start_time)

def selection_sort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end_time = time.time()
    print("Selection sort time: ", end_time - start_time)

def make_array(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 1000))
    return arr

# 100
# 500
# 1000
# 5000
# 10000

# Array dengan 100 data
print("----- Array dengan 100 data -----")
array_length = 100
arr = make_array(array_length)
bubble_sort(arr)
selection_sort(arr)

# Array dengan 500 data
print("\n----- Array dengan 500 data -----")
array_length = 500
arr = make_array(array_length)
bubble_sort(arr)
selection_sort(arr)

# Array dengan 1000 data
print("\n----- Array dengan 1000 data -----")
array_length = 1000
arr = make_array(array_length)
bubble_sort(arr)
selection_sort(arr)

# Array dengan 5000 data
print("\n----- Array dengan 5000 data -----")
array_length = 5000
arr = make_array(array_length)
bubble_sort(arr)
selection_sort(arr)

# Array dengan 10000 data
print("\n----- Array dengan 10000 data -----")
array_length = 10000
arr = make_array(array_length)
bubble_sort(arr)
selection_sort(arr)
