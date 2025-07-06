def coin_change(coins: list[int], amount: int) -> int:
    """
    Returns the minimum number of coins needed to make the given amount.
    Args:
        coins: List of positive integer coin denominations.
        amount: Non-negative integer target amount.
    Returns:
        Minimum number of coins needed, or -1 if impossible.
    """
    # Input validation
    if not coins and amount > 0:
        return -1
    if amount < 0 or any(coin <= 0 for coin in coins):
        return -1
    
    # Initialize DP array: dp[i] = min coins to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Fill DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    # Return result: -1 if impossible, otherwise the minimum coins
    return dp[amount] if dp[amount] != float('inf') else -1

# Test cases
test_cases = [
    ([1, 2, 5], 11),  # Expected: 3
    ([2], 3),         # Expected: -1
    ([1], 0),         # Expected: 0
    ([], 1),          # Expected: -1
    ([1, 5, 10], 15)  # Expected: 2
]

for coins, amount in test_cases:
    result = coin_change(coins, amount)
    print(f"For coins {coins} and amount {amount}, minimum coins needed: {result}")