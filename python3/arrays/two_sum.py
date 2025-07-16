class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            if target - num in num_map:
                return [index, num_map[target - num]]
            num_map[num]= index