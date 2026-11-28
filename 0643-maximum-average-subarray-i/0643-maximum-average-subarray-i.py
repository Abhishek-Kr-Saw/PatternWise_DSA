class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        res,sum = 0,0
        for i in range(0,k):
            sum += nums[i]

        res = sum / k

        for i in range(k,len(nums)):
            sum += nums[i] - nums[i-k]
            res = max(res, sum/k)

        return res
        