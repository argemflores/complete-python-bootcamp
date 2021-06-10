# array_count9

# Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    count_9 = 0
    
    for num in nums:
        if num == 9:
            count_9 += 1
    
    return count_9
