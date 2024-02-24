def factorial_dynamic(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]

# Example usage:
number = 5
fact = factorial_dynamic(number)
print("Factorial of", number, "is", fact)
