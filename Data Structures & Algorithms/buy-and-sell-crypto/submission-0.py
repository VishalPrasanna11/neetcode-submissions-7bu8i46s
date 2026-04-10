class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                cur_profit = prices[right] - prices[left]
                max_profit = max(max_profit, cur_profit)  # Update max_profit
            else:
                left = right  # Update left pointer to the current right

            right += 1  # Move the right pointer to the next day

        return max_profit
