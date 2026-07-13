class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<int>> dp (n, vector<int>(amount + 1, 1e9));
        for(int i = 0; i < n; i++) dp[i][0] = 0;
        for(int j = 0; j <= amount; j++) {
            if (j % coins[0] == 0) dp[0][j] = (j/coins[0]);
        }
        
        for(int i = 1; i < n; i++) {
            for(int j = 0; j <= amount; j++) {
                int skip = dp[i-1][j];
                int take = 1e9;
                if(j >= coins[i]) {
                    take = 1 + dp[i][j - coins[i]];
                }
                dp[i][j] = min(skip, take);
            }
        }

        return dp[n-1][amount] if dp[n-1][amount] != 1e9 else -1;
    }
};
