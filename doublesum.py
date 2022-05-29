def add(nums,target):
    for i in range(len(nums)):
        for x in range(i,len(nums)):
            if nums[i] + nums[x] == target:
                return[i,x];

print(add([1,1,3,2],5))
