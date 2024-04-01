# This problem was asked by Google.
# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

# Define a Counting Elements in an array
def counting(A,m):
    n = len(A)
    count = [0]*(m+1)
    for i in range(n):
        count[A[i]] += 1 
    return count
    
#Define a Duplicate Find by PigeonHole Principal
def dupFind(A):
    n = len(A)
    count = counting(A,n)
    for i in range(0,n):
        if count[i] == 2:
            return i 
    
A = [1,2,3,4,5,6,7,8,9,3]
print(dupFind(A))
#Output: 3
