class Solution:
    # Runtime: 74.01%  Memory Usage: 5.27%
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 if s==0 else 0 for s in l[::-1]] for l in A]

if __name__ == "__main__":
    pass