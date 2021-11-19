from functools import lru_cache
class Solution:
    @lru_cache()
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        else :
            if n%2 == 0:
                return self.integerReplacement(int(n/2))+1
            else:
                return min(self.integerReplacement(n-1),self.integerReplacement(n+1))+1

s = Solution()
print(s.integerReplacement(3))
