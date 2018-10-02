import dataset

arr = dataset.random

def selectionsort(arr):
    # For each number...
    for i in range(0, len(arr)):
        minInd = i
        min = arr[i]
        # Find the minimum...
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                minInd = j
        # Swap the minimum with the current element
        temp = arr[i]
        arr[i] = arr[minInd]
        arr[minInd] = temp

selectionsort(arr)
print(arr)