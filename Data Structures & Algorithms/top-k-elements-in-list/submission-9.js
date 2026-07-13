class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // I know that I have to count the occurences of each element, then make a bucket array with counts of each as indices and the actualy values as an array inside that
        const count = {};
        let bucket = Array.from({length: nums.length + 1}, () => []);
        let res = [];
        for (const n of nums) {
            count[n] = (count[n] || 0) + 1;
        }
        for (const key of Object.keys(count)) {
            bucket[count[key]].push(parseInt(key));
        }
        for(let i = nums.length; i > 0; i--) {
            if(bucket[i].length && res.length <= k) {
                for(const c of bucket[i]) {
                    res.push(c);
                    if(res.length == k) {
                        return res;
                    }
                }
            }
        }
    }
}
