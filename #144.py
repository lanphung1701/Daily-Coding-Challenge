# This problem was asked by Google.

# Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

# If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

# Follow-up: If you can preprocess the array, can you do this in constant time?

def findNearestLarger(arr, index):
    back = index - 1
    key_back = 0
    forw = index + 1
    key_forw = 0
    
    while back >= 0:
        if arr[back] > arr[index]:
            key_back = back
            break
        else:
            back = back - 1
    
    while forw < len(arr):
        if arr[forw] > arr[index]:
            key_forw = forw
            break
        else:
            forw = forw + 1 
    
    if key_back >= 0 or key_forw < len(arr):
        b = index - key_back
        f = key_forw - index
        
        if b > f:
            return key_forw
        elif b < f:
            return key_back
        elif b == f:
            return key_back, key_forw
    else:
        return None

arr = [4,1,3,5,6]
res = findNearestLarger(arr, 3)
print(res)
