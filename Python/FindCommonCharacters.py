class Solution:
    def commonChars(self, A):
        if len(A) == 0:
            return []
        result = []
        for char in A[0]:
            result.append(char)
        for i in range():

        return result

if __name__ == "__main__":
    test_cases = [
        ["bella", "label", "roller"],
        ["cool", "lock", "cook"]
    ]
    s = Solution()
    for test_case in test_cases:
        print(s.commonChars(test_case))
