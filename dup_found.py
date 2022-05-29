# def dup_found(num):
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False
A = Solution();
print(A.containsDuplicate([1,1,1,2,3,4]))