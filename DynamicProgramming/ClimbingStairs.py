def climbStairs(self, n: int) -> int:
    distinctPaths = 0
    distinctPaths = climbStairsRec(n, 0)
    return distinctPaths

def climbStairsRec(n, curStep):
    if (curStep > n):
        return 0
    elif (curStep == n):
        return 1
    
    return climbStairsRec(n, curStep + 1) + climbStairsRec(n, curStep + 2) 