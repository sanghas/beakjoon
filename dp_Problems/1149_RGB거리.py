import sys

def sol(dp,arr) :
    next_dp = dp.copy()
    next_dp[0] = arr[0] + min(dp[1],dp[2])
    next_dp[1] = arr[1] + min(dp[0],dp[2])
    next_dp[2] = arr[2] + min(dp[1],dp[0])
    return next_dp

N = int(input())
dp = [0] * 3
for i in range(N):
    RGB = list(map(int,sys.stdin.readline().split()))
    if i == 0:
        dp = RGB
    else:
        dp = sol(dp,RGB)
print(min(dp))
