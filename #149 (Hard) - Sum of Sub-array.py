# This problem was asked by Goldman Sachs.
# Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.
# You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.

######### SOLUTION:
# Define sum_arr to caculate sum of a list or array
def sum_arr(arr):
    sum = 0
    for i in range (0,len(arr)):
        sum = sum + arr[i]
    
    return sum

# Use slice list and apply sum_arr() method
def slice_sum(arr, i, j):
    temp_list = arr[i:j]
    return sum_arr(temp_list)

arr = [1,2,3,4,5]
res = slice_sum(arr, 1, 3)
print(res)
# RETURN 5
