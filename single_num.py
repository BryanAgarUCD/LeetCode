# def single_num(nums):
#     result = 0
#     if len(nums) != 0:
#         for number in nums:
#             result = result ^ number

#     print(result)
#     return result

# single_num([4,4,4,4,4,2,1,1,1,1])


from typing import List

class Solution:
    def singleNumber(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
        return ans
        
ans = Solution()
print(ans.singleNumber([4,1,2,1,2,3,3]))