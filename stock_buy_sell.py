class solution:
    def maxProfit(self, prices):
        print(prices)
        profit = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            if temp < 0:
                continue
            else:
                profit += temp
        return profit

prices = list(map(int, input("prices = ").split()))
ans = solution()
print(ans.maxProfit(prices))