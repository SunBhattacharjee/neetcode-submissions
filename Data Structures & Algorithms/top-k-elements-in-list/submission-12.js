class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {};
        let bucket = Array.from({length: nums.length + 1}, () => []);
        for (const n of nums) {
            count[n] = (count[n] || 0) + 1;
        }
        for (const key of Object.keys(count)) {
            bucket[count[key]].push(key);
        }
        let res = [];
        for(let i = nums.length; i > 0; i--) {
            if(bucket[i]) {
                for(const c of bucket[i]) {
                    res.push(c);
                    if(res.length == k) return res;
                }
            }
        }
    }
}
