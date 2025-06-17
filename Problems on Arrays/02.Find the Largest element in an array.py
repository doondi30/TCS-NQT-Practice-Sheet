#method 1
class Solution:
    def largestElement(self, nums):
        maxi = float("-inf")
        for i in nums:  
            if i > maxi:  
                maxi = i
        return maxi

s = Solution()
nums = [3, 3, 6, 1]
print(s.largestElement(nums))

#method 2
# Intuition:
# We can sort the array in ascending order, hence the largest element will be at the last index of the array. 

# Approach: 
# Sort the array in ascending order.
# Print the (size of the array -1)th index.
# DryRun: 
# Before sorting: arr[] = {2,5,1,3,0};

# After sorting: arr[] = {0,1,2,3,5};

# Hence answer : arr[sizeofthearray-1] =5

# Code
# Complexity Analysis

# Time Complexity: O(N*log(N))

# Space Complexity: O(n)

nums=[3,3,6,1]
nums.sort()
print(nums[-1])
