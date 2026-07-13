class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        // [1, 2, 4, 6]
        let res = Array(nums.length).fill(0);
        for(const n in nums) {
            let prod = 1;
            for(const m in nums) {
                if(n === m) {
                    continue;
                }
                prod = prod * nums[m];
            }
            res[n] = prod;
        }
        return res;
    }
}
