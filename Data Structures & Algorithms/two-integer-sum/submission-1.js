class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const checked = new Map();
        for(let i = 0; i < nums.length; i++) {
            let diff = target - nums[i];
            
            if(checked.has(diff)){
                return [checked.get(diff), i];
            } else {
                checked.set(nums[i] ,i);
            }
        }
        return [];
    }
}
