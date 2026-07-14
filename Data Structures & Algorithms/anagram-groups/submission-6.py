class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            count[key].append(s)
        return list(count.values())