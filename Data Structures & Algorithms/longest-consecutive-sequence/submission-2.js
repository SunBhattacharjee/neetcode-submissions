class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const set = Set(nums)
        let longest = 0;
        for(const n of nums) {
            if(!(set.has(n-1))) {
                let length = 0;
                while(set.has(n + length)) {
                    length += 1;
                }
                longest = Math.max(longest, length)
            } 
        }
        return longest;
    }
}
