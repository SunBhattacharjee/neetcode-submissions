class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            key = tuple(set(s))
            count[key].append(s)
        print(count)
        return count.values()