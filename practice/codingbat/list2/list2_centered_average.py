# centered_average

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    # get min and max numbers
    min_num = min(nums)
    max_num = max(nums)

    # remove first occurrence only
    nums.remove(min_num)
    nums.remove(max_num)

    # compute for average of remaining numbers
    final_ave = 0

    for num in nums:
        final_ave += num

    return final_ave // len(nums)
