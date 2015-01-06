# 3.2: How would you design a stack which, in addition to push and pop,
# also a has a function min which returns the minimum element? push, pop
# and min should all operate in O(1) time.

# The first idea I had was to use a min-heap in addition to a stack.
# However, a min-heap does not have O(1) removal time, which would be
# needed for the pop operation.

# Further thought presented the following idea: use two stacks, one for
# the elements in the stack, and the other for the minima. Each time a
# new element is pushed onto the main stack, if that element is less
# than the current minimum, it is also pushed onto the stack for minima.
# Then the min function just returns the current minima (or the top of
# the minima stack). Whenever a minimum is popped off the main stack,
# it is also popped off the minima stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.minima = []

    def push(self, item):
        if len(self.minima) == 0 or item < self.minima[-1]:
            self.minima.append(item)

        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.minima[-1]:
            self.minima.pop()

        return item

    def min(self):
        return self.minima[-1]


stack = MinStack()
for n in [2, 7, 1, 3]:
    stack.push(n)

print(stack.min())      # should be 1
stack.pop()
stack.pop()
print(stack.min())      # should be 2
