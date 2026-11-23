class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum == 0:
                    temp_list = [nums[i], nums[left], nums[right]]
                    res.append(temp_list)
                    left += 1
                    right -= 1
                    while left < n and nums[left] == nums[left - 1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1

                elif triplet_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res
