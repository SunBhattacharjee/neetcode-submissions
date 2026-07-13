class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let s_count = {};
        let t_count = {};
        s.split("").forEach((c) => {
            if(!s_count[c]) {
                s_count[c] = 1;
            } else {
                s_count[c]++;
            }
        })
        t.split("").forEach((c) => {
            if(!t_count[c]) {
                t_count[c] = 1;
            } else {
                t_count[c]++;
            }
        })
        
        const s_keys = Object.keys(s_count);
        const t_keys = Object.keys(t_count);

        if(s_keys.length != t_keys.length) {
            return false;
        }

        for(const k of s_keys){
            if(!(k in t_count)) {
                return false;
            }
            if(s_count[k] != t_count[k]) {
                return false;
            }
        }

        return true;
    }
}
