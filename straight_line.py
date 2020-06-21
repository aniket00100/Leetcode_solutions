import math
class Solution:

    def calculate_answer(self, coordinates):
        co_length = len(coordinates)
        if co_length == 2:
            return True
        if coordinates[0][1] == 0 and coordinates[1][1] == 0:
            # handle the x-axis code
            for points in coordinates:
                if points[1] != 0:
                    return False

        if coordinates[0][0] == 0 and coordinates[1][0] == 0:
            # handle the y-axis code
            for points in coordinates:
                if points[0] != 0:
                    return False
        if coordinates[0][0] == coordinates[1][0]:
            # parallel to y-axis
            x = coordinates[0][0]
            for points in coordinates:
                if points[0] != x:
                    return False

        slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        for i in range(2, co_length):
            denominator = (coordinates[i-1][0] - coordinates[i][0])
            if denominator == 0:
                temp_slope = math.inf
            else:
                temp_slope = (coordinates[i-1][1] - coordinates[i][1]) / denominator
            if temp_slope != slope:
                return False

        return True

coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]
ans = Solution()
print(ans.calculate_answer(coordinates))