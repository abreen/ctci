# 9.2: Imagine a robot sitting on the upper left corner of an X by Y
# grid. The robot can only move in two directions: right and down. How
# many possible paths are there for the robot to go from (0, 0)
# to (X, Y)?

# Let's alter the problem slightly so that we are going from (X, Y) to
# (0, 0). This will not affect the number of possible paths, but will
# make this function's base cases easier to write.

# The function below will form a call tree where each path in the tree
# is a valid path taken by the robot. Each leaf in the call tree is
# a call to robot_paths(0, 0), where the value 1 is sent back up to
# the tree, counting that path.

def robot_paths(x, y):
    if x == 0 and y == 0:
        return 1                            # already here

    if x == 0:
        return robot_paths(x, y - 1)        # can only go down from here

    if y == 0:
        return robot_paths(x - 1, y)        # only go sideways from here

    return robot_paths(x - 1, y) + \
           robot_paths(x, y - 1)

# This function runs in O(2^n), however, since all paths have to be
# enumerated. However, once a given number of paths has been found
# from a particular coordinate, we should memoize that number so that
# subsequent calls to the function are faster.

paths = {}
def robot_paths(x, y):
    if (x, y) in paths:
        return paths[(x, y)]

    if x == 0 and y == 0:
        paths[(x, y)] = 1
        return 1

    if x == 0:
        result = robot_paths(x, y - 1)
        paths[(x, y)] = result
        return result

    if y == 0:
        result = robot_paths(x - 1, y)
        paths[(x, y)] = result
        return result

    result = robot_paths(x - 1, y) + \
             robot_paths(x, y - 1)
    paths[(x, y)] = result
    return result

# This memoized version allows large inputs (e.g., (30, 300)) to be computed
# more quickly.
