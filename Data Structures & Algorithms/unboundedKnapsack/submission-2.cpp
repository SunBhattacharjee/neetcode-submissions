class Solution {
public:
    int maximumProfit(vector<int>& val, vector<int>& wt, int cap) {
        int n = wt.size();
        vector<int> prev(cap + 1, 0);
        vector<int> cur(cap + 1, 0);

        for(int j = 0; j <= cap; j++) {
            if(wt[0] <= j) {
                int fits = j/wt[0];
                prev[j] = val[0] * fits;
            }
        }

        for(int i = 1; i < n; i++) {
            for(int j = 1; j <= cap; j++) {
                int skip = prev[j];
                int take = 0;

                if(wt[i] <= j) {
                    take = val[i] + cur[j - wt[i]];
                }

                cur[j] = max(skip, take);
            }
            prev = cur;
        }

        return prev[cap];
    }
};
