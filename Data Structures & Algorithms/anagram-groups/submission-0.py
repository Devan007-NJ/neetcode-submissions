class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            j=list(i)
            j.sort()
            new_i="".join(j)
            if new_i in hashmap:
                hashmap[new_i].append(i)
            else:
                hashmap[new_i]=[i]
        return list(hashmap.values())