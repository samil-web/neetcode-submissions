class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            diff = target-num
            if diff in seen:
                indexes= [seen[diff], i]
                return sorted(indexes)
            seen[num] = i
        return False