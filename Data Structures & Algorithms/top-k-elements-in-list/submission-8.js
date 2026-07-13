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
        for (const n of nums) {
            count[n] = (count[n] || 0) + 1;
        }
        const keys = Object.keys(count);
        // [1,2,3]
        for (const i in keys) {
            bucket[count[keys[i]]].push(count[i]);
        }
        console.log(bucket);
    }
}
