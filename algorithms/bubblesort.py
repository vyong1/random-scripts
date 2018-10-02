import dataset

def bubbleSort(arr):
    iterations = 0
    isSorted = False
    # Keep going until isSorted is true
    while(isSorted == False):
        # Assume isSorted is true until we have
        # to swap elements
        isSorted = True
        for i in range(0, len(arr) - 1):
            iterations += 1
            # Swap if out of order
            if(arr[i] > arr[i + 1]):
                isSorted = False
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    return iterations

arr = dataset.reverse
iterations = bubbleSort(arr)
print(iterations, arr)