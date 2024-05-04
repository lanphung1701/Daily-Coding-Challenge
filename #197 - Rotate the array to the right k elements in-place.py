# This problem was asked by Amazon.
# Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

def solution(arr,k):
    n = len(arr)
    temp = [0]*n 
    
    for i in range(n):
        if (i+k) >= n:
            temp[(i+k)%n] = arr[i]
        if (i+k) < n:
            temp[i+k] = arr[i]
    return temp

arr = [3,5,2,5,7,8,3]
k = 3
print(solution(arr,k)) #Return [7,8,3,3,5,2,5]
