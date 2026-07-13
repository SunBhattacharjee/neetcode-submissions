class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        let prefix = 1;
        let res = Array(n).fill(0);
        for (let i = 1; i < n; i++) {
            res[i] = prefix;
            prefix = prefix * nums[i];
        }
        console.log(res);
        let suffix = 1;
        for (let i = n - 1; i >= 0; i--) {
            res[i] = res[i] * suffix;
            suffix = suffix * nums[i];
        }
        return res;
    }
}
