Ransom Note

You showed:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen={}
        for ch in magazine:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
Core Idea

Count frequencies of characters.

Pattern

Hash Map Frequency Counting

Correct Thought Process
Count characters in magazine.
For every character in ransomNote:
Character must exist.
Frequency must be > 0.
Reduce count.
Template
count = {}

for ch in magazine:
    count[ch] = count.get(ch, 0) + 1

for ch in ransomNote:
    if ch not in count or count[ch] == 0:
        return False

    count[ch] -= 1

return True
Time Complexity
O(n + m)
Key Learning

Frequency counting appears everywhere:

Anagrams
Character counting
Inventory problems
String matching
