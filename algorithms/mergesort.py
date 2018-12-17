def merge(arr1, arr2):
	merged = []
	while(len(arr1) != 0 and len(arr2) != 0):
		if(arr1[0] < arr2[0]):
			merged.append(arr1.pop(0))
		else:
			merged.append(arr2.pop(0))
	
	# Add remaining list (there should only be 1)
	while(len(arr1) != 0):
		merged.append(arr1.pop(0))
	while(len(arr2) != 0):
		merged.append(arr2.pop(0))
	
	return merged

def merge_sort(arr):
	if(len(arr) == 0):
		return arr

	# Slice array
	toMerge = []
	for i in range(0, len(arr)):
		toMerge.append([arr[i]])
	
	# Merge
	while(len(toMerge) > 1):
		left = toMerge.pop(0)
		right = toMerge.pop(0)
		toMerge.append(merge(left, right))
	
	return toMerge[0]

arr1 = [5, 4, 3, 2, 1]
arr2 = [1, 1, 1, 2, 1, 3]
arr3 = []
arr4 = [5, 10, 15, 20, 25]
arr5 = [25, 20, 15, 10, 5]


print(merge_sort(arr1))
print(merge_sort(arr2))
print(merge_sort(arr3))
print(merge_sort(arr4))
print(merge_sort(arr5))
