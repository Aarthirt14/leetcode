# Problem: Intersection of Two Arrays
# Platform: LeetCode
# Pattern: Arrays + Hashing (Set)
# Difficulty: Easy
#
# Key Idea:
# - Use a set for O(1) lookup
# - Convert one array to set
# - Traverse the other array
# - Store result in a set to ensure uniqueness
#
# Time Complexity: O(n + m)
# Space Complexity: O(n)
#
# Why this works:
# - Set removes duplicates automatically
# - Fast lookup avoids nested loops

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)

        return list(result)
