class Solution:
    def commonChars(self, A):
        if len(A) == 0:
            return []
        result = []
        for char in A[0]:
            result.append(char)
        result.sort()
        for i in range(1, len(A)):
            p = 0
            q = 0
            new_list = []
            for char in A[i]:
                new_list.append(char)
            new_list.sort()
            while (p < len(result) and q < len(new_list)):
                if result[p] == new_list[q]:
                    p += 1
                    q += 1
                elif result[p] > new_list[q]:
                    q += 1
                else: 
                    result.remove(result[p])
            if q == len(new_list):
                result = result[:p]
        return result

if __name__ == "__main__":
    test_cases = [
        ["bella", "label", "roller"],
        ["cool", "lock", "cook"]
    ]
    s = Solution()
    for test_case in test_cases:
        print(s.commonChars(test_case))
