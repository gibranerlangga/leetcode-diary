# source: https://leetcode.com/problems/generate-parentheses/?envType=featured-list&envId=top-interview-questions

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

def generateParenthesis(n):
    if n == 1:
        return ['()']
    else:
        result = []
        for i in range(1, n):
            for j in generateParenthesis(i):
                print('j', j)
                for k in generateParenthesis(n-i):
                    print('k', k)
                    result.append(j+k)
        return result
    
print(generateParenthesis(3))
print(generateParenthesis(4))
