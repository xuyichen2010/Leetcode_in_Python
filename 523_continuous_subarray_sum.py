# Brute
# O(n^3)

# Optimized Brute
# Prefix Sum
# O(n^2)
# O(n)
# Use a map to store prefix sum up to index i
# So we can calculate sum at j as in sum[j] - sum[i] + nums[i]



# One pass
# O(n)
# O(min(n,k)) up to min(n,k) different pairs

# a%k = x
# b%k = x
# (a - b) %k = x -x = 0

# For anybody is confused about map.put(0,-1);
# In the case nums = [1, 5] k = 6, at i=1, sum % k is 0,
# so we need a key '0' in the map, and it must be comply with the continuous condition,
# i - map.get(sum) > 1, so we give an arbitrary value of -1.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        sum_to_index = {0:-1}
        running_sum = 0
        for i in range(0, len(nums)):
            running_sum += nums[i]
            if k != 0:
                running_sum %= k
            if running_sum in sum_to_index:
                if (i - sum_to_index[running_sum] > 1): # Making sure the subarray is greater than 1
                    return True
            else:
                sum_to_index[running_sum] = i
        return False