class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<int>> dp (n, vector<int>(amount + 1, 0))
        
        for(int i = 1; i < n; i++) {
            for(int j = 0; j <= amount; j++) {
                int skip = dp[i-1][j];
                int take = INT_MAX;
                if(j >= nums[i]) {
                    take = dp[i][j - nums[i]];
                }
            }
        }

        return dp[n-1][amount];
    }
};
