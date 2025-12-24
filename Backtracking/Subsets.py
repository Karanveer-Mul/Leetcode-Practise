nums = [1,2,3]
output = []
subset = []
def backtrack(length=0):
    if length == len(nums):
        output.append(subset[:])
        return

    # create the subset and then either extend or not to the final
    subset.append(nums[length])
    backtrack(length+1)

    subset.pop()
    backtrack(length+1)

backtrack()
print(output) 