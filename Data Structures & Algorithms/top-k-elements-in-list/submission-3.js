class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const newSet = new Set(nums);
        let count = {};
        for(let i = 0; i < nums.length; i++) {
            for(let j = 1; j <= newSet.length; j++) {
                if(!count[j]) {
                    count[j] = [nums[i]];
                } else {
                    count[j].push(nums[i])
                }
            }
        }
        return count[k];
        // 1 2 2 3 3 3
        // 1 : [1, 2, 3]
        // 2 : [2, 3]
        // 3 : [3]
        // ...
    }
}
