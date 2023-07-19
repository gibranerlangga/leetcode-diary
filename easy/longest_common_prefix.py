# source: https://leetcode.com/problems/longest-common-prefix/?envType=featured-list&envId=top-interview-questions

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Constraints:
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# Pseudocode:

# 1. Find the shortest string in the list
# 2. Iterate over the characters in the shortest string
# 3. For each character, check if it is in the same position in all the other strings
# 4. If it is, add it to the result string
# 5. If it is not, return the result string


def longestCommonPrefix(strs):
        result = ""
        strs_sorted = sorted(strs)

        first = strs_sorted[0]
        last = strs_sorted[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result

strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = [""]
print(longestCommonPrefix(strs))