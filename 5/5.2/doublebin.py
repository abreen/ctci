# 5.2: Given a real number between 0 and 1 (e.g., 0.72) that is passed in
# as a double, print the binary representation. If the number cannot be
# represented accurately in binary with at most 32 characters, print "ERROR".

# I wasn't quite sure what this one was asking, so I went right to its
# solution. I re-implemented it in Python:

def print_double(d):
    if d == 0.0:
        print("0.0")
        return

    s = "0."
    while d > 0:
        if len(s) > 32:
            print("ERROR")
            return

        r = d * 2
        if r >= 1:
            s += "1"
            d = r - 1
        else:
            s += "0"
            d = r

    print(s)
