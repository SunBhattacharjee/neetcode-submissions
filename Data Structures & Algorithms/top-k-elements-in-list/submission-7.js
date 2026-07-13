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
        const values = Object.values(count);
        for (const i in values.length) {
            bucket[count[i]].push(count[i]);
        }
        console.log(bucket);
    }
}
