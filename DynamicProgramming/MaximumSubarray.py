class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * (len(nums)+1) 
        maxSum = nums[0]
        for i in range(1, len(nums)):
            curSum = dp[i-1] + nums[i]
            dp[i] = max(curSum, nums[i])
            maxSum =  max(dp[i], maxSum)
        return maxSum