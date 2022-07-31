maxnum = 1000000000

def solution(n) :
    ans = 0
    dp = [0,1,1,1,1,1,1,1,1,1]
    new_dp = [0,0,0,0,0,0,0,0,0,0]
    for j in range(n-1):
        for i in range(len(dp)):
            if i == 0:
                new_dp[i] = dp[i+1] 
            elif i == 9:
                new_dp[i] = dp[i-1] 
            else :
                new_dp[i] = (dp[i-1] + dp[i+1]) 

        dp = new_dp.copy()
        new_dp = [0,0,0,0,0,0,0,0,0,0]
    return sum(dp) % maxnum

n = int(input())
print(solution(n))