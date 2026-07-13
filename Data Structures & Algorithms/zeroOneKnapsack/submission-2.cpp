class Solution {
private:
    int f(int ind, int cap, vector<int>& wt, vector<int>& val, int n, vector<vector<int>>& dp) {
        if(ind == n) return 0;
        if(dp[ind][cap] != -1) return dp[ind][cap];

        int notTake = f(ind + 1, cap, wt, val, n, dp);
        int take = INT_MIN;

        if(cap >= wt[ind]) {
            take = val[ind] + f(ind + 1, cap - wt[ind], wt, val, n, dp);
        }

        return dp[ind][cap] = max(take, notTake);
    }
public:
    int maximumProfit(vector<int>& profit, vector<int>& weight, int capacity) {
        int n = weight.size();
        vector<vector<int>> dp(n, vector<int>(capacity + 1, -1));
        return f(0, capacity, weight, profit, n, dp);
    }
};
