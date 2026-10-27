class CountSquares:

    def __init__(self):
        self.countP = defaultdict(int)
        self.points = []

    def add(self, point: list[int]) -> None:
        self.countP[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: list[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:
                continue
            
            res += (self.countP[(x, py)] * self.countP[(px, y)])
        
        return res
