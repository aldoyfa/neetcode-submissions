class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)//2
        while n >= 0 and n <= len(nums) - 1:
            if nums[n] < target:
                n += 1
                if n > len(nums)-1:
                    break
                elif nums[n] > target: 
                    break
            elif nums[n] > target:
                n -= 1
                if nums[n] < target or n < 0:
                    break
            else:
                return n
        return -1