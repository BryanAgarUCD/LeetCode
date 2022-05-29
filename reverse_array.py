
nums = [1,1,1,1,12,2,3,3,4,5,6,7,8]  
def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1
        print(nums)
k = 0
k %= len(nums)
reverse(nums, 0, len(nums))
reverse(nums, 0, k)
reverse(nums, k, len(nums))



