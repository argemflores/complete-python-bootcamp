# has22

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
    counter = 0
    is_found = False

    for x in nums:
        # 2 found, add to counter
        if x == 2:
            counter += 1
        else:
            # not 2, reset counter
            counter = 0

        # 2, 2 found, counter = 2 already
        if counter == 2:
            is_found = True
            break

    return is_found
