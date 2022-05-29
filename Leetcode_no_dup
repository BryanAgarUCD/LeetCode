# // LEETCODE - ARRAY, NO DUPS

# Remove Duplicates from Sorted Array
# -----------------------------------
# Given a sorted array nums, remove the duplicates in-place such that
# each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.


class Solution(object):
    def removeDuplicates(nums):
        if len(nums) <= 1:
            return len(nums)
        new_length = 0

        for i in range(len(nums)):

            # print(i)
            if nums[i] != nums[new_length]:
                
                new_length += 1
                nums[new_length] = nums[i]
                # print(new_length)
        print(new_length)
        return new_length + 1,
    removeDuplicates([1,2,2,3,3,2,2,2,2,2,23,3,3,3,3,3,3,4,4,4,4,4])