from typing import List

import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price1 = math.inf
        price2 = -math.inf
        max_profit = 0
        for price in prices:
            if price < price1:
                price1 = price
                price2 = -math.inf
            if price > price2:
                price2 = price

            if price2 - price1 > max_profit:
                max_profit = price2 - price1
        if max_profit == math.inf or max_profit == -math.inf:
            max_profit = 0
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    prices = [7, 6, 4, 3, 1]
    prices = [2, 4, 1]
    # prices = [1, 2]
    print(Solution().maxProfit(prices=prices))
