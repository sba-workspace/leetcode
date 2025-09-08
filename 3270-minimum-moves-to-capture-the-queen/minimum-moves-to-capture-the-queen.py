class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Rook in same row as Queen
        if a == e:
            # Bishop blocks Rook or not
            return 2 if c == a and (b < d < f or b > d > f) else 1
        # Rook in same column as Queen
        if b == f:
            # Bishop blocks Rook or not
            return 2 if d == f and (a < c < e or a > c > e) else 1
        # Bishop in same up-diagonal as Queen
        if c + d == e + f:
            # Rook blocks Bishop or not
            return 2 if a + b == c + d and (c < a < e or c > a > e) else 1
        # Bishop in same down-diagonal as Queen
        if c - d == e - f:
            # Rook blocks Bishop or not
            return 2 if a - b == c - d and (c < a < e or c > a > e) else 1
        return 2