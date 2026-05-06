class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k, cnt = 0, 0
        for i in range(len(s)):
            for j in range(k, len(t)):
                if t[j] == s[i]:
                    k = j + 1
                    cnt += 1
                    break
        return cnt == len(s)