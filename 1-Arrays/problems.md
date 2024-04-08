[Remove Duplicates (Easy)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1226766586/)

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

[Remove Element (Easy)](https://leetcode.com/problems/remove-element/)
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

[Contains Duplicate (Easy)](https://leetcode.com/problems/contains-duplicate/)
```python
def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) # check if set conversion smaller
```
```python
  def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset: # seen a duplicate
                return True
            # otherwise, add to hashset, so we can check for dups later
            hashset.add(n)
        return False
```

[Valid Anagram (Easy)](https://leetcode.com/problems/valid-anagram/description/)
```python
def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        return s_dict == t_dict
```

```python
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}

        for i in range(0, len(s)):
            # get(key, value), value is default if key doesn't exist
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        return s_dict == t_dict
```