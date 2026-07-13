class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const maxOccurence = nums.length;
        const count = {};
        let bucket = Array.from({length: maxOccurence + 1}, () => []);
        let res = [];
        for (const num of nums) {
            count[num] = (count[num] || 0) + 1;
        }
        for(const key of Object.keys(count)) {
            bucket[count[key]].push(parseInt(key));
        }
        for(let i = maxOccurence; i > 0; i--)  {
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
