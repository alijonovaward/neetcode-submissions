class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f = defaultdict(int)
        for i in nums:
            f[i] += 1
            if f[i] > 1:
                return True
        return False