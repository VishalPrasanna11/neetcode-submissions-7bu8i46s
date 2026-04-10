class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if (len(intervals) == 0):
            return 0

        # Sort the intervals based on end time
        intervals.sort(key=lambda x: x[1])
        count = 1

        prev_interv = 0

        for i in range(1,len(intervals)):

            if ( intervals[i][0]>=intervals[prev_interv][1]):
                prev_interv = i
                count += 1

        return len(intervals)-count