# Brute Force 1
# Check all subarray and compute sum
# O(n^3) n^2 num of arrays and O(n) to computer each sum
# O(1)

# Brute Force 1
# Use DP to pre-calculate the sum
# So it takes O(1) to calculate each sum
# O(n^2)
# O(n)
'''
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        for (int i = 1; i <= nums.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                if (sum[end] - sum[start] == k)
                    count++;
            }
        }
        return count;
    }
}
'''

# Without Space
# Running Sum
# O(1) space
'''
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }
}
'''

# Hashmap Prefix sum
# determine the number of times a subarray with sum kk has occured upto the current index
# O(n)
# O(n)

class Solution(object):
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        sum_to_count = {0:1}
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            res += sum_to_count.get(curr_sum-k, 0)
            print(res)
            sum_to_count[curr_sum] = sum_to_count.get(curr_sum, 0) + 1
        return res

# If all positive interger
# O(N)
# O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        p1 = 0
        p2 = 0
        curr_sum = nums[0]
        count = 0
        while p2 < len(nums) and p1 < len(nums):
            print(p1, p2, curr_sum)
            if curr_sum < k:
                p2 += 1
                if p2 >= len(nums):
                    break
                curr_sum += nums[p2]
            elif curr_sum > k:
                curr_sum -= nums[p1]
                p1 += 1
            else:
                count += 1
                p2 += 1
                if p2 >= len(nums):
                    break
                curr_sum += nums[p2]
                curr_sum -= nums[p1]
                p1 += 1
        return count

