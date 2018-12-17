import math

def binary_partition(arr, preferred_partition_size = 1, partitioned_list = []):
	# Base Case: No longer able to be partitioned
	if (len(arr) == preferred_partition_size
		or len(arr)/2 < preferred_partition_size):
		partitioned_list.append(arr)
	# Recursive Case: Continue partitioning
	else:
		begin = 0
		mid = len(arr)//2
		end = len(arr)
		
		# Partition array in half
		left = arr[begin : mid]
		right = arr[mid : end]
		binary_partition(left, preferred_partition_size, partitioned_list)
		binary_partition(right, preferred_partition_size, partitioned_list)
	return partitioned_list
	
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6]
arr3 = [38, 27, 43, 3, 9, 82, 10]

print(binary_partition(arr1, 1, []))
print(binary_partition(arr1, 2, []))
print(binary_partition(arr1, 3, []))
print(binary_partition(arr1, 4, []))
print(binary_partition(arr1, 5, []))
