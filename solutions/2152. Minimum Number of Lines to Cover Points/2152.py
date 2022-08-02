class Solution:
  def minimumLines(self, points: List[List[int]]) -> int:
    n = len(points)
    allCovered = (1 << n) - 1
    maxLines = n // 2 + (n & 1)

    def getSlope(p: List[int], q: List[int]) -> Tuple[int, int]:
      dx = p[0] - q[0]
      dy = p[1] - q[1]
      if dx == 0:
        return (0, p[0])
      if dy == 0:
        return (p[1], 0)
      d = gcd(dx, dy)
      x = dx // d
      y = dy // d
      return (x, y) if x > 0 else (-x, -y)

    @lru_cache(None)
    def dfs(covered: int) -> int:
      if covered == allCovered:
        return 0

      ans = maxLines

      for i in range(n):
        if covered >> i & 1:
          continue
        for j in range(n):
          if i == j:
            continue
          # connect points[i] with points[j]
          newCovered = covered | 1 << i | 1 << j
          slope = getSlope(points[i], points[j])
          # mark points covered by this line
          for k in range(n):
            if getSlope(points[i], points[k]) == slope:
              newCovered |= 1 << k
          ans = min(ans, 1 + dfs(newCovered))

      return ans

    return dfs(0)
