nums = [1,2,3,1]
k = 3

numSet = set()

for i in range(len(nums)):
    if nums[i] in numSet:
        print(True)
        break
    numSet.add(nums[i])

    if len(numSet) > k:
        numSet.remove(nums[i-k])

print(False) 