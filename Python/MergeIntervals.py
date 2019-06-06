class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals
        else:
            intervals.sort(key=lambda x: x[1])
            intervals.sort(key=lambda x: x[0])
            i = 0
            max_value = len(intervals)
            while i < max_value:
                if i + 1 >= len(intervals):
                    break
                if intervals[i+1][0] <= intervals[i][1]:
                    for j in range(i + 1, len(intervals)):
                        if intervals[j][0] > intervals[i][1]:
                            intervals = intervals[: i] + [[intervals[i][0], max(intervals[j-1][1], intervals[i][1])]] + intervals[j:]
                            break
                    else:
                        intervals = intervals[: i] + [[intervals[i][0], max(intervals[j][1], intervals[i][1])]]
                else:
                    i += 1
        return intervals
                    

if __name__ == "__main__":
    s = Solution()
    inputs = [
        # [[1,3],[2,6],[8,10],[15,18]],
        # [[1,4],[4,5]],
        # [[1,4],[0,4]],
        # [[1,4],[2,3]],
        # [[1,4],[0,2],[3,5]],
        [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]
    ]
    for intervals in inputs:
        print(s.merge(intervals))