class Solution {
private:
    int f(vector<int>& nums, int i, int j) {
        int minusTwo = 0;
        int minusOne = 0;

        for(int x = i; x <= j; x++) {
            int cur = max(minusTwo + nums[x], minusOne);
            minusTwo = minusOne;
            minusOne = cur;
        }

        return minusOne;
    }
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        return max(f(nums, 1, n-1), f(nums, 0, n-2));
    }
};
