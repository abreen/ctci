# 5.1: You are given two 32-bit integers, N and M, and two bit positions,
# i and j. Write a method to insert M into N such that M starts at bit j
# and ends at bit i. You can assume that the bits j through i have enough
# space to fit all of M. That is, if M = 10011, you can assume that there
# are at least 5 bits between j and i.

# My note: these bit positions are inclusive, and the least significant
# bit is bit 0.

def insert_into(n, m, i, j):
    # need sequence of j - i + 1 ones
    mask = 0
    for i in range(j - i + 1):
        mask |= 1 << i

    # take the desired bits from m
    m &= mask

    # shift m and mask so we start at i
    mask = mask << i
    m = m << i

    # inverting the mask here keeps the rest of n
    solution = (n & ~mask) | m

    # we return both the value of the solution and a string, for ease
    return solution, bin(solution)

# My guess is that there's another clever way to get j - i + 1 many
# ones by finding the smallest power of 2 greater than that sum and
# subtracting one. But I'm not certain it would be more efficient...
