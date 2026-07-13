class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let count = {};
        let res = [];
        for(let i = 0; i < strs.length; i++) {
            const key = strs[i].split("").sort().join("");
            if(!count[key]) {
                count[key] = [strs[i]];
            } else {
                count[key].push(strs[i]);
            }
        }
        const keys = Object.keys(count);
        for(const k of keys) {
            res.push(count[k]);
        }
        return res;
    }
}
