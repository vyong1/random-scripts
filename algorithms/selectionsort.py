import dataset

def selectionsort(arr):
    iterations = 0
    # For each number...
    for i in range(0, len(arr)):
        iterations += 1
        minInd = i
        min = arr[i]
        # Find the minimum...
        for j in range(i, len(arr)):
            iterations += 1
            if arr[j] < min:
                min = arr[j]
                minInd = j
        # Swap the minimum with the current element
        temp = arr[i]
        arr[i] = arr[minInd]
        arr[minInd] = temp
    return iterations

arr = dataset.random
iterations = selectionsort(arr)
print(iterations, arr)