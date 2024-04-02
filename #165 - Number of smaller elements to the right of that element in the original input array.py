# This problem was asked by Google.
# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1


def smallestToright(A):
    n = len(A)
    count = [0]*n
    
    for i in range(0,len(A)):
        j = i+1
        while j < len(A):
            if A[j] < A[i]:
                count[i] += 1 
            j +=  1
            
        if i == len(A)-1:
            count[i] = 0
            
    return count

A = [3,4,9,6,1]
print(smallestToright(A)) #OUTPUT: [1, 1, 2, 1, 0]
