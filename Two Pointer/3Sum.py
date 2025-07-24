nums = [-1,0,1,2,-1,-4]
sortedNums = sorted(nums)

result = []
lenNums = len(nums)

for i, num in enumerate(sortedNums):

    if i > 0 and num == sortedNums[i-1]:
        continue

    left = i+1
    right = lenNums - 1

    while left < right:
        numSum = num + sortedNums[left] + sortedNums[right]

        if numSum > 0:
            right -= 1
        elif numSum < 0:
            left += 1
        else:
            result.append([num, sortedNums[left], sortedNums[right]])

            left += 1
            while left < right and sortedNums[left] ==  sortedNums[left-1]:
                left += 1

print(result) 
