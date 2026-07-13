class Solution {
private:
    int f(int ind, int cap, vector<int>& wt, vector<int>& val, int n) {
        if(ind == n) return 0;

        int notTake = f(ind + 1, cap, wt, val, n);
        int take = INT_MIN;

        if(cap >= wt[ind]) {
            take = val[ind] + f(ind + 1, cap - wt[ind], wt, val, n);
        }

        return max(take, notTake);
    }
public:
    int maximumProfit(vector<int>& profit, vector<int>& weight, int capacity) {
        int n = weight.size();
        return f(0, capacity, weight, profit, n);
    }
};
