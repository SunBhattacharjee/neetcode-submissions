class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length){
            return false
        }

        let s1 = {}
        let s2 = {}

        for (let i = 0; i < s.length; i++) {
            s1[s[i]] = (s1[s[i]] || 0) + 1;
            s2[t[i]] = (s2[t[i]] || 0) + 1;
        }

        for (let x in s1){
            if(s1[x] !== s2[x]){
                return false
            }
        }

        return true
    }
}
