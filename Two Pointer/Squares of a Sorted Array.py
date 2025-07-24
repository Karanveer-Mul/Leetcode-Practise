nums = [-4,-1,0,3,10]

numLen = len(nums)
i = 0
j = numLen - 1

result = [0] * numLen

while numLen >= 0:
    # compare squared i and j elements and swap
    a = nums[i] ** 2
    b = nums[j] ** 2

    if a > b:
        result[numLen-1] = a
        i += 1
    else:
        result[numLen-1] = b
        j -= 1
    numLen -= 1

    if i == j:
        result[numLen-1] = nums[i] ** 2
        break

print(result)