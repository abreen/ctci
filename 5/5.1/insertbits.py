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
    for x in range(j - i + 1):
        mask |= 1 << x

    # make mask start at i
    mask = mask << i

    # clear relevant sequence of bits in n
    n &= ~mask

    # shift m into place
    m = m << i

    # inverting the mask here keeps the rest of n
    solution = n | (m & mask)

    # we return both the value of the solution and a string, for ease
    return solution, bin(solution)

N, M, I, J = 0b10000000, 0b101, 0, 2
print(insert_into(N, M, I, J))

# My guess is that there's another clever way to get j - i + 1 many
# ones by finding the smallest power of 2 greater than that sum and
# subtracting one. But I'm not certain it would be more efficient...

# Note: the book's solution is cooler than that (I'm paraphrasing here,
# and converting to Python):

def insert_into(n, m, i, j):
    ones = 0xffffffff

    # we're pushing the ones left so that the first zero is at j
    left = ones << (j + 1)

    # right should have its first i bits set to 1
    right = (1 << i) - 1

    # e.g., 11100001 (for j = 5, i = 1)
    mask = left | right

    # clear bits to make way for n
    n &= mask

    # inverting the mask here keeps the rest of n
    solution = n | (m << i)

    # we return both the value of the solution and a string, for ease
    return solution, bin(solution)

print(insert_into(N, M, I, J))
