"""
Problem: Valid Anagram
Pattern: Hashing
Data Structure: Dictionary (Hash Map)

Approach:
- If lengths differ, return False
- Count character frequencies from the first string
- Decrease counts while scanning the second string
- If any character is missing or overused, return False

Time Complexity: O(n)
Space Complexity: O(1)  # since alphabet size is constant
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True
