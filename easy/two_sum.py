## source: https://leetcode.com/problems/two-sum/?envType=featured-list&envId=top-interview-questions

def twoSum(nums, target):
    n = len(nums)
    num_ref = {nums[i]: i for i in range(n)}

    for i in range(n):
        substract_val = target - nums[i]
        if substract_val in num_ref and num_ref[substract_val] != i:
            return [i, num_ref[substract_val]]
    return []


nums = [2,7,11,15]
target = 9
## desired output: [0, 1]
nums1 = [3,2,3]
target1 = 6

print(twoSum(nums, target))
print(twoSum(nums1, target1))