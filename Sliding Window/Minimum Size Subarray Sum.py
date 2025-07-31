nums = [2,3,1,2,4,3]
target = 7
left = 0
arrSum = 0
output = float('inf')
for right in range(len(nums)):
    arrSum += nums[right]

    while arrSum >= target:
        output = min(output, right-left+1)
        arrSum -= nums[left]
        left += 1
if output == float('inf'):
    print(0)
else:
    print(output) 