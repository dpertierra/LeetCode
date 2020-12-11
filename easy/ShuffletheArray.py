def shuffle(nums, n):
    out =[]
    for i in range(n): 
        out.insert(2*i, nums[i])
        out.insert(2*i+1,nums[n+i])
    return out

def shuffle2(nums,n):
    out = []
    for x,y in zip(nums[:n], nums[n:]):
        out+=[x,y]
    return out
print(shuffle([2,5,1,3,4,7], 3))
#[2,3,5,4,1,7]
print(shuffle([1,2,3,4,4,3,2,1], 4))
#[1,4,2,3,3,2,4,1]
print(shuffle([1,1,2,2], 2))
#[1,2,1,2]