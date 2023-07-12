## source: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
## Do not return anything, modify nums1 in-place instead.

def merge_sorted_array(nums1, nums2, m, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
## desired output: [1, 2, 2, 3, 5, 6]

print(merge_sorted_array(nums1, nums2, m, n))