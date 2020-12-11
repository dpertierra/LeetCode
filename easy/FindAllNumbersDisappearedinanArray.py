def findDisappearedNumbers(nums):
    out = []
    # for i in range(len(nums)):
    #     if nums[abs(nums[i])-1] > 0:
    #         nums[abs(nums[i])-1] *= -1
    
    # for i in range(len(nums)):
    #     if nums[i] > 0:
    #         out.append(i+1)
    # return out
    setNums = set(nums)
    for i in range(1, len(nums)+1):
        if i not in setNums:
            out.append(i)
    return out

# print(findDisappearedNumbers([4,4,2,6,8,2,1,1]))
print(findDisappearedNumbers([1,1]))