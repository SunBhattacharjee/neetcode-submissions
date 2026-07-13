class Solution {
public:
    int maximumProfit(vector<int>& val, vector<int>& wt, int cap) {
        int n = wt.size();
        vector<vector<int>> dp(n, vector<int>(cap + 1, 0));

        for(int j = 0; j <= cap; j++) {
            if(wt[0] <= j) dp[0][j] = val[0];
        }

        for(int i = 1; i < n; i++) {
            for(int j = 1; j <= cap; j++) {
                int skip = dp[i-1][j];
                int take = 0;

                if(wt[i] <= j) {
                    take = val[i] + dp[i][j - wt[i]];
                }

                dp[i][j] = max(skip, take);
            }
        }

        return dp[n-1][cap];
    }
};
