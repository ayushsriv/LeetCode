class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=itemgetter(0))
        copy = [intervals[0]]
        for interval in intervals[1:]:         
            if interval[0]<=copy[-1][1]:
                copy[-1][1] = max(interval[1], copy[-1][1])
            else:
                copy.append(interval)
        return copy
                
                