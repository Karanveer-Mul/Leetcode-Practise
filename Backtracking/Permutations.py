
nums = [1,2,3]
output = []

def backtrack(sub, subnums):
    if len(sub) == len(nums):
        output.append(sub[:])
        return

    for i in range(len(subnums)):
        new_sub = sub + [subnums[i]]
        new_subnums = subnums[:i] + subnums[i+1:]
        backtrack(new_sub, new_subnums)
    
backtrack([], nums)
print(output)