
dp=[[-1 for _ in range(1001)] for _ in range(1001)]
def knapsack(wt,values,W,n):
    if n==0 or W==0:
        return 0
    if dp[n][W]!=-1:
        return dp[n][W]
    if wt[n-1]<=W:
        dp[n][W]=max(values[n-1]+knapsack(wt,values,W-wt[n-1],n-1),knapsack(wt,values,W,n-1))
    elif wt[n-1]>W:
        dp[n][W]=knapsack(wt,values,W,n-1)
    return dp[n][W]

wt=[4,5,1]
values=[1,2,3]
W=4
n=len(wt)
print(knapsack(wt,values,W,n))