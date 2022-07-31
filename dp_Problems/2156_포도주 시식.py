import sys

def solution(dp,arr):
    dp[0] = arr[0]
    if len(arr)>1:
        dp[1] = arr[0]+arr[1]
    if len(arr)>2:
        dp[2] = max( arr[0]+arr[2] , arr[1]+arr[2] , dp[1])
    if len(arr)>3:
        for i in range(3,len(arr)):
            dp[i] = max( dp[i-2]+arr[i] , dp[i-3]+arr[i-1]+arr[i] )
            dp[i] = max( dp[i-1], dp[i])
    return max(dp)

N =int(input())
dp = [0]*N
arr = [0]*N
for i in range(N):
    arr[i] = int(sys.stdin.readline())
print(solution(dp,arr))