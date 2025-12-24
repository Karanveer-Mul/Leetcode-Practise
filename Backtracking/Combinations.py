n = 4
k = 2
output = []
sub = []

def backtrack(start):
    if len(sub) == k:
        output.append(sub[:])
        return

    for num in range(start, n+1):
        sub.append(num)
        backtrack(num+1)
        sub.pop() # The secret sauce, we are creating all possible outcomes and removing the unwanted one

backtrack(1)
print(output)