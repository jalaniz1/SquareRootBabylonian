#import math

__author__ = 'frankdrevin'
def compute_sqrt(n):
    "Computer Square root *without* math library functions"

    # The target is a 0(log n) or constant time (1) implementation
    # Result is to be truncated down to the nearest integer 7.1 or 7.9 produce 7
    # Attempting to use the babylonian method going for a log n implementation
    if n <= 0:
        return 0  # Error?
    r1 = n / 2  # Guess, Babylonian step 1
    while r1*r1 > n:  # Still Too big
            r1 /= 2
    while r1*r1 < n:  # Too small
        if ((r1 * 1.5) * r1) < n:  # If we're not exceeding our boundary
            r1 *= 1.5
        else:  # If not then we're close enough at this point
            break

    while True:  # Repeat Step 2 until it's precise
        oldr1 = r1  # Save
        if (r1*r1) != n:  # This *can* produce imprecise comparison...
                          # If r1*r1 is 159.99999999999997 and n is 160, will return False
            r1 = (r1 + n/r1)/2  # Babylonian step 2
        else:  # We found our match!
            break
        if oldr1 == r1:  # Using caution to prevent infinite loop
            break
    result = r1  # For clarity of anyone reading... Unnecessary. But there you go!
    return result



n = 160
# For comparison between my square root and the python library square root
# print("Python Math Library %d" % math.sqrt(n))
print("My function %d" % compute_sqrt(n))

