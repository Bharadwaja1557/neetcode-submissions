class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        # Hierholzer's Algorithm

        adj = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")
        return res[::-1]