"""
LeetCode: Top K Frequent Elements
Pattern: Hashing
"""

from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    return [num for num, count in freq.most_common(k)]


# Example
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
