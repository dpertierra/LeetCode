# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# https://leetcode.com/problems/two-sum/

def twosumSorted(nums, target): #Assuming the list is sorted we can do this in O(n) time. 
                                #if we need to sort the list first the time would be O(nlogn)
    indEnd = len(nums)-1
    indStart = 0
    listR = []
    for i in range(len(nums)):
        if indStart == indEnd:
            return listR
        if  abs(nums[indStart]) + abs(nums[indEnd]) < abs(target):
            indStart+=1
        elif abs(nums[indStart]) + abs(nums[indEnd]) > abs(target):
            indEnd-=1
        elif abs(nums[indStart]) + abs(nums[indEnd]) == abs(target):
            listR.append(indStart)
            listR.append(indEnd)
            return listR
    return listR

def twosum(nums, target):
    auxNum=0 
    secondIndex=-1
    listR=[]
    for index, num in enumerate(nums):
        if len(listR) >= 2:
            return listR
        auxNum = target - num
        try:
            secondIndex=nums.index(auxNum, index+1)
            if secondIndex != 0:
                listR.append(index)
                listR.append(secondIndex)
        except ValueError:
            continue
        return listR

print(twosumSorted([2,7,11,15], 9)) # Caso 1
print(twosumSorted([2,3,4],6)) # Caso 2
print(twosumSorted([3,3],6)) # Caso 3
print(twosumSorted([-1,-2,-3,-4,-5],-8)) # Caso 4
