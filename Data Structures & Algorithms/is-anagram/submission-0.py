class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = defaultdict(int)
        for c in s:
            f[c] += 1
        for c in t:
            f[c] -= 1
        for k in f.values():
            if k != 0:
                return False
        return True