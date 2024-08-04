from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.
        You can return the answer in any order."""
        
        index = 0

        for num in nums:
          nedded_number = target - num
          subindex = [i for i, value in enumerate(nums) if value == nedded_number and i != index]

          if subindex:
            if len(subindex) > 1:
              return [index, subindex[0]]
            else:
              return [index, subindex[0]]
          
          index += 1
           

solution = Solution()
print(solution.twoSum([2,7,11,7], 9))