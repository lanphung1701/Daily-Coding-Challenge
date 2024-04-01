# This problem was asked by Facebook.

# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.

def binReverse(bin):
    bin = bin[::-1]
    return bin

bin = '1111 0000 1111 0000 1111 0000 1111 0000'
print(binReverse(bin))
#Output: 000 111 000 111 000 111 000 111
