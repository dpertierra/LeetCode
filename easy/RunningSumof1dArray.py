def runningSum(nums):
    out=[]
    for i, num in enumerate(nums):
        if i == 0:
            out.append(num)
        else:
            out.append(out[i-1]+num)
    return out

print(runningSum([1,2,3,4]))
print(runningSum([3,1,2,10,1]))
print(runningSum([3,1,2,10,1]))