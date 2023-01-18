from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrm = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            angrm[ss].append(s)
        return list(angrm.values())