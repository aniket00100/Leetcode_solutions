class Solution:

    def productExceptSelf(self, nums):
        length = len(nums)
        left = []
        right = []
        left.append(1)
        right.append(1)
        for i in range(1, length):
            left.append(left[i-1] * nums[i-1])
            right.append(right[i - 1] * nums[length - i])
        for i in range(0, length):
            nums[i] = left[i] * right[length - i - 1]
        return nums

nums = list(map(int, input("nums = ").split()))
ans = Solution()
print(ans.productExceptSelf(nums))