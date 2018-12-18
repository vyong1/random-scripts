'''
Solution for https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 1000
-100 ≤ A[i] <= 100

Sample Input:
2               # Number of test cases
3               # Array size
1 2 3           # Array values
4               # Array Size
-1 -2 -3 -4     # Array values

'''

def solution(arr):
    if (len(arr) == 0):
        return 0
    
    highest_sum = arr[0]
    cumulative_sum = 0
    
    i = 0
    while(i < len(arr)):
        cumulative_sum += arr[i]
        
        if (cumulative_sum > highest_sum):
            highest_sum = cumulative_sum;
        
        if (cumulative_sum < 0):
            cumulative_sum = 0 # Restart sum
        
        i += 1
    
    return highest_sum


# This input parsing is just for the website submission
    
import sys

# Parse input
i = 1
test_cases = []
for line in sys.stdin:
    if (i == 0): # Number of test cases
        pass
    elif (i % 2 == 0): # Number of elements in the array
        pass
    if (i != 1 and i % 2 == 1): # Array values
        split = line.split(' ')
        test_case = []
        for value in split:
            if(value != '\n'):
                test_case.append(int(value))
        test_cases.append(test_case)
    i += 1

for test_case in test_cases:
    print(solution(test_case))
    

'''
# Custom Test cases

# 6
arr1 = [1, 2, 3] 

# -1
arr2 = [-1, -2, -3, -4]

# 4
arr3 = [-1, 2, -3, 4]

# 12
arr4 = [3, -2, 4, -2, 5, -3, 7]

# -1
arr5 = [-4, -3, -2, -1]


print(solution(arr1))
print(solution(arr2))
print(solution(arr3))
print(solution(arr4))
print(solution(arr5))
'''