# sum13

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    total_sum = 0
    flag_13 = False

    for x in nums:
        # number is less than 13
        if x < 13:
            # following 13, skip
            if flag_13:
                flag_13 = False
                continue

            # add to total sum
            total_sum += x
        else:
            # skip 13 from total sum
            flag_13 = True

    return total_sum
