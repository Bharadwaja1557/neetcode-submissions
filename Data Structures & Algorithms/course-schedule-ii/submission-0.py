class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereq = {c: [] for c in range(numCourses)}

        for c, p in prerequisites:
            prereq[c].append(p)
        
        cycle = set() # "currently visiting" set
        visit = set() # "already visited" set

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for p in prereq[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res