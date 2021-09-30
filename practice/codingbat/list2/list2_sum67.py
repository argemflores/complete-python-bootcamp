# sum67

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    total_sum = 0
    is_ignored = False

    for x in nums:
        # 6 found, activate ignore flag
        if x == 6:
            is_ignored = True
            continue
        elif x == 7 and is_ignored:
            # 7 found and ignored, deactivate ignore flag
            is_ignored = False
            continue

        # number not ignored, add to total sum
        if not is_ignored:
            total_sum += x

    return total_sum
