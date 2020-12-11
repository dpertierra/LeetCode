def kidsWithCandies(candies, extraCandies):
    out = []
    maxCandies = max(candies)
    for num in candies:
        if num+extraCandies >= maxCandies:
            out.append(True)
        else: 
            out.append(False)
    return out

print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10))