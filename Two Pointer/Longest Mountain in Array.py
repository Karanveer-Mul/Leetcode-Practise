arr = [2,1,4,7,3,2,5]
arrLen = len(arr)

left = 0
right = 0
result = 0

for i in range(1, arrLen-1):
    if (arr[i-1] < arr[i] > arr[i+1]):
        left = i
        right = i

        while (left > 0 and arr[left] > arr[left-1]):
            left -= 1
        while (right < (arrLen - 1) and arr[right] > arr[right+1]):
            right += 1
        result = max(result, right - left + 1)

print(result) 