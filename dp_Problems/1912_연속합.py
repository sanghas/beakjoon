import sys

def maxValue(arr) :
    dp = [arr[0]]
    for i in range(1,len(arr)) :
        dp.append(max(dp[i-1]+arr[i],arr[i]))   
    return max(dp)

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
print(maxValue(arr))