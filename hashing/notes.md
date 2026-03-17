## Contains Duplicate – Learning Notes

Initial thought:
- Compare each element with all others (O(n²)) → inefficient

Improvement:
- Use a set to track previously seen values
- Reduce time complexity to O(n)

Key takeaway:
- When the problem asks about "already seen" elements,
  hashing is usually the right pattern.

## Valid Anagram – Learning Notes

Initial thought:
- Check if both strings contain the same characters
- Realized that character frequency matters, not just presence

Key observation:
- An anagram requires the same characters with the same counts
- If lengths differ, anagram is impossible

Correct approach:
- Use a hash map (dictionary) to store character frequencies from the first string
- Traverse the second string and decrement counts
- If a character is missing or overused, return False

Why hashing works:
- Allows O(1) average lookup for character counts
- Ensures efficient frequency tracking

Key takeaway:
- When a problem involves matching frequencies of elements,
  hashing with a dictionary is the correct pattern

  ## Two Sum – Learning Notes
Initial thought

Check every pair of numbers to see if they add up to the target

This requires two loops → O(n²) time complexity

Improvement

Use a hash map (dictionary) to store numbers and their indices while iterating.

Correct approach

Traverse the array once.

For each number, calculate the complement:

𝑐
𝑜
𝑚
𝑝
𝑙
𝑒
𝑚
𝑒
𝑛
𝑡
=
𝑡
𝑎
𝑟
𝑔
𝑒
𝑡
−
𝑛
𝑢
𝑚
complement=target−num

Check if the complement already exists in the hash map.

If yes → return the indices.

Why hashing works

Hash maps allow O(1) lookup for complements.

This reduces time complexity to O(n).

Key takeaway

When a problem asks for finding pairs that satisfy a condition, hashing can help store previously seen values for quick lookup.
## Group Anagrams – Learning Notes
Initial thought

Compare every string with every other string to check if they are anagrams.

This results in O(n²) comparisons.

Improvement

Use hashing to group strings with the same character pattern.

Correct approach

For each string:

Sort the characters.

Use the sorted string as a key in a dictionary.

Append the original word to that key’s list.

Example:

eat → aet
tea → aet
tan → ant

Dictionary:

{
"aet": ["eat", "tea"],
"ant": ["tan"]
}
Why hashing works

Strings with the same sorted representation belong to the same group.

Key takeaway

When grouping elements based on similar patterns, hashing with a dictionary is very effective.

## Top K Frequent Elements – Learning Notes
Initial thought

Count the frequency of each number manually and then sort them.

Sorting all elements may be inefficient.

Improvement

Use a hash map to count frequencies first.

Correct approach

Use a dictionary to store frequency counts.

num_count[num] += 1

Extract the top k elements based on frequency.

Example:

nums = [1,1,1,2,2,3]
k = 2

Frequency map:

{
1:3,
2:2,
3:1
}

Result:

[1,2]
Why hashing works

Quickly counts occurrences in O(n) time.

Key takeaway

When a problem involves frequency counting, hashing with a dictionary is the best pattern.

