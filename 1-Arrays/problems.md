[Remove Duplicates](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1226766586/)

Solution:
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # let LP be the left pointer, which stores
        # the location of the last replaced value in nums.
        LP = 1
        # let RP be the right pointer, which stores
        # the location of where it is checking
        RP = 0

        # traverse through the array
        # since non-decreasing, duplicates only occur when
        # nums[RP] == nums[RP - 1]
        for RP in range(1, len(nums)):
            if nums[RP] != nums[RP - 1]: # not a duplicate
                nums[LP] = nums[RP]
                LP += 1

        # LP is k, that is, the number of unique elements
        return LP
```

[Remove Element](https://leetcode.com/problems/remove-element/)
```python
def removeElement(self, nums: List[int], val: int) -> int:
        LP = 0 # replacement pointer
        
        # traverse the entire array
        for i in range(0, len(nums)):
            if nums[i] != val: # if not equal
                nums[LP] = nums[i] # replace at the start of the array
                LP += 1
        return LP
```