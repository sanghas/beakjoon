def solution(arr):
    dp=[1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

N = int(input())
arr = list(map(int,input().split()))
print(solution(arr))