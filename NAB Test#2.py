# You are given a string S consisting of N letters 'a' and/or 'b'. In one move, you can swap one letter for the other ('a' for 'b' or 'b' for 'a').
# Write a function solution that, given such a string S, returns the minimum number of moves required to obtain a string containing no instances of three identical consecutive letters.
# Examples:
# 1. Given S = "baaaaa", the function should return 1. The string without three identical consecutive letters which can be obtained in one move is "baabaa".
# 2. Given S = "baaabbaabbba", the function should return 2. There are four valid strings obtainable i two moves: for example, "bbaabbaabbaa".
# 3. Given S = "baabab", the function should return 0.
# Write an efficient algorithm for the following assumptions:
# ⚫N is an integer within the range [0..200,000];
# ⚫String S is made only of the characters 'a' and/or 'b'.


#Solution: Compare every each 3 consecutive elements to check if they are similar
def solution(S):
    times = 0
    i = 0
    while i < len(N)-2:
        #If 3 elements in a row are the same, swapping move increases by 1 and index moves to the next 3 elements
        if S[i] == S[i+1] and S[i+1] == S[i+2]:
            times += 1
            i += 3
        else:
            i += 1
    return times


S = 'baaaaa'
print(solution(S)) #Output: 1
