# Leetcode

class Solution:

    # Second attempt!!!
    # def find_the_judge(self, N, trust):
    #     if N == 2:
    #         return trust[0][1]
    #     people = dict()
    #     for i in range(1, N + 1):
    #         people.update({i: 0})
    #
    #     for pair in trust:
    #         people.update({pair[1]: people.get(pair[1]) + 1})
    #         if people.get(pair[1]) >= N - 1:
    #             return pair[1]
    #
    #     print(people)
    #     return -1

    def find_the_judge(self, N, trust):
        if len(trust) == 1:
            return trust[0][1]
        trusted_people = dict()
        i = 1
        while i < N + 1:
            trusted_people.update({i: set()})
            i += 1
        for pair in trust:
            b = trusted_people.get(pair[1])
            b.add(pair[0])
        everybody_trusts = None
        for key in trusted_people.keys():
            if len(trusted_people.get(key)) == N - 1:
                everybody_trusts = key
        for pair in trust:
            if pair[0] == everybody_trusts:
                everybody_trusts = None
        if  everybody_trusts:
            return everybody_trusts
        return -1



trust = [[1,2],[2,1]]
N = 2
# print(trust)
ans = Solution()
print(ans.find_the_judge(N, trust))
