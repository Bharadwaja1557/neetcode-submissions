class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += "�"
        return res

    def decode(self, s: str) -> List[str]:
        res = ""
        arr = []
        for c in s:
            if c != "�":
                res += c
            else:
                arr.append(res)
                res = ""

        return arr