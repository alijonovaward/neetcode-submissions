class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = -1
        for i in range(n - 1, -1, -1):
            h = arr[i]
            arr[i] = mx
            mx = max(h, mx)
        # arr[-1] = -1
        return arr