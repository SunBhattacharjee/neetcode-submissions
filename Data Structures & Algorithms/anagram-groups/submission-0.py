class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}
        output = []
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            
            if tuple(key) not in visited:
                visited[tuple(key)] = [word]
            else:
                visited[tuple(key)].append(word)
                
        for a in visited.items():
            output.append(a[1])
        return output