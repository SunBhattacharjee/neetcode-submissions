class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        nums = [1,2,2,3,3,4,4,4,4];
        const newSet = new Set(nums);
        let count = {};
        let freq = Array.from({length: nums.length + 1}, () => []);
        
        for(const n of nums) {
            count[n] = (count[n] || 0) + 1;
        }

        for(const n in count) {
            freq[count[n]].push(parseInt(n))
        }
        console.log(freq);
        const res = [];
        for (let i = freq.length - 1; i > 0; i--) {
            for(const n of freq[i]) {
                res.push(n);
                if(res.length == k) return res;
            }
        }

    }
}
