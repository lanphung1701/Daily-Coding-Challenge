# You are given a positive integer N. Your task is to find the smallest integer greater than N that does not contain two identical consecutive digits.
# For example, given N = 1765, the smallest integer greater than N is 1766. However, in 1766 the last two digits are identical. The next integer, 1767, does not contain two identical consecutive digits, and is the smallest integer greater than 1765 that fulfils the condition. Note that the second and fourth digits in 1767 can both be 7 as they are not consecutive.
# Write a function:
# def solution (N) 
# that, given an integer N, returns the smallest integer greater than N that does not contain two identical consecutive digits.
# Examples:
# 1. Given N = 55, the function should return 56. It is the smallest integer greater than 55 and it does not contain two consecutive digits that are the same.
# 2. Given N = 1765, the function should return 1767, as explained above.
# 3. Given N = 98, the answer should be 101. Both 99 and 100 contain two identical consecutive digits, but 101 does not.
# 4. Given N = 44432, the answer should be 45010.
# 5. Given N = 3298, the answer should be 3401.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..1,000,000,000].


#Define a function that detects a number that has identical consecutive elements
def consecutiveFind(A):
    x = str(A)
    for i in range(0,len(x)-1):
        if x[i] == x[i+1]:
            return 1 

def solution(N):
    temp = N+1
    while True:
        x = consecutiveFind(temp)
        if x == 1:
            temp += 1
        else:
            return temp
            
N = 1765
print(solution(N)) #Output: 1767
