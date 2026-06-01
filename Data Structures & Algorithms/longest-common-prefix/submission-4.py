class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]

        fin = ""
        k = 1

        strs.sort(key=len)

        while(k<len(strs[0])+1):
            for i in range(1, len(strs)):
                if strs[0][:k] in strs[i]:
                    if i==len(strs)-1:
                        fin = strs[0][:k]
                else:
                    break
            k = k + 1

        return fin
