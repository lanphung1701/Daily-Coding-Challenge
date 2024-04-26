# This problem was asked by Google.
# Given an array of elements, return the length of the longest subarray where all its elements are distinct
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

def solution(arr):
    n = len(arr)
    count = [0]*n
  
    for i in range(n):
        count[arr[i]] += 1
      
    res = len(count) - count.count(0)
    return res

arr = [5, 1, 3, 5, 2, 3, 4, 1]
print(solution(arr)) # Return 5
