class Solution:

    def is_bad_version(self, val):
        print('executing is_bad_version')
        if val >= 3:
            return True
        return False

    def first_bad_version(self, n):
        # a.k.a binary_search
        mid = n // 2

        # if n <= 2:
        #     if not self.is_bad_version(1):
        #         return 2
        #     else:
        #         return 1

        if self.is_bad_version(mid):
            return self.true_search(1, mid)
        else:
            return self.true_search(mid, n)

    def true_search(self, start, end):
        mid = (end // 2) + 1
        while True:
            if self.is_bad_version(mid):
                end = mid
            else:
                start = mid
            if not self.is_bad_version(end - 1) and self.is_bad_version(end):
                return end
            mid = start + (end - start) // 2

ans = Solution()
print(ans.first_bad_version(3))