class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        max_diff = float('inf') 
        res = float('inf')
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while(left < right):
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)

                if total == target:
                    return total
                elif total < target:
                    if max_diff > diff:
                        max_diff = diff
                        res = total
                    left += 1
                else:
                    if max_diff > diff:
                        max_diff = diff
                        res = total
                    right -= 1

        return res

