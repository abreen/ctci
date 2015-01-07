# 9.1: A child is running up a staircase with n steps, and can hop either
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count how
# many possible ways the child can run up the stairs.

# This can be done recursively.

def hop_ways(n):
    if n <= 0:
        # no way to hop at all
        return 0

    if n == 1:
        # only one way: hop 1 stair
        return 1

    if n == 2:
        # either hop 1 stair twice, or hop 2
        return 2

    if n == 3:
        # hop 1 stair three times, or hop 2 and 1 (two ways)
        # or hop 3 stairs
        return 1 + 2 + 1

    # recursive case: the number of ways we can do n stairs
    # is by hopping 1 step here, and then finding the rest,
    # or by hopping 2 steps here, etc.
    return hop_ways(n - 1) + hop_ways(n - 2) + hop_ways(n - 3)

# The recursive case of this function runs in O(3^n), since each recursive
# call will retrace path down the call tree to a base case. This makes
# this function extremely inefficient.

# A simple way to optimize the function is to use memoization.

def memoized(func):
    memo = {}

    def f(arg):
        if arg in memo:
            return memo[arg]
        rv = func(arg)
        memo[arg] = rv
        return rv

    return f

hop_ways = memoized(hop_ways)

# This simple approach now allows extremely large values of n (e.g., 300)
# to be solved quickly, by using O(n) extra space in the dictionary.
