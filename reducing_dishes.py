# BRUTE FORCE

#######version 1########

# class Solution:
#     def maxSatisfaction(self, satisfaction):
#         satisfaction.sort()
#         max = 0
#         current_sum = 0
#         for i in range(0, len(satisfaction)):
#             temp_list = satisfaction[i:]
#             for j in range(0, len(temp_list)):
#                 current_sum += temp_list[j] * (j+1)
#             if current_sum > max:
#                 max = current_sum
#             current_sum = 0
#         return max

#########################################################################
# Version 2
#########################################################################
class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        current_sum = 0

        last_sum = satisfaction[-1] * len(satisfaction)
        # print("last_sum = ", last_sum)
        for i in range(0, len(satisfaction)):
            if satisfaction[i] >= 0:
                break
            current_sum += satisfaction[i] * (i + 1)

        current_sum = abs(current_sum)
        if current_sum <= last_sum:
            # print("first current_sum = ", current_sum)
            current_sum = 0
            for i in range(0, len(satisfaction)):
                current_sum += satisfaction[i] * (i + 1)
        else:
            current_sum = 0
            for i in range(0, len(satisfaction)):
                current_sum += abs(satisfaction[i] * (i + 1))
                if current_sum >= last_sum:
                    # print("2nd current_sum = ", current_sum)
                    # print("intermediate satisfaction = ", satisfaction[i:])
                    break
            # print("i = ", i)
            dish_list = satisfaction[i+1:]
            # print("dish_list = ", dish_list)
            current_sum = 0
            for i in range(0, len(dish_list)):
                current_sum += dish_list[i] * (i+1)

        if current_sum < 0:
            current_sum = 0

        return current_sum

nums = list(map(int, input("nums = ").split()))
ans = Solution()
print(ans.maxSatisfaction(nums))

