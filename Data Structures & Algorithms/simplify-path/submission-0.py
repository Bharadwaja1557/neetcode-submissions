class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = path.split("/")

        for p in res:
            if p != "" and p != ".":
                if p == "..":
                    if stack:
                        stack.pop()
                else:               
                    stack.append(p)

        res = "/" + "/".join(stack)
        return res

