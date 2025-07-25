arr = [4,2,1,3]
sortedArr = sorted(arr)
minAbsDif = sortedArr[1] - sortedArr[0]
output = []
for i in range(1, len(sortedArr)):
    absDif = abs(sortedArr[i] - sortedArr[i-1])

    if minAbsDif > absDif:
        output.clear()
        minAbsDif = absDif

    if minAbsDif == absDif:
        output.append([sortedArr[i-1], sortedArr[i]])
print(output)