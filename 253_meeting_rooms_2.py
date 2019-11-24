 # https://leetcode.com/problems/meeting-rooms-ii/solution/

# Ask Clarifying: IS IT OK IF THE START TIME OF THE NEXT EVENT IS EQUAL TO THE ENDING TIME
# OF THE FIRST
# Arranging the meetings according to their start times helps us know the natural order of
# meetings throughout the day. However, simply knowing when a meeting starts doesn't tell
# us much about its duration.

# We also need the meetings sorted by their ending times because an ending event essentially
# tells us that there must have been a corresponding starting event and more importantly,
# an ending event tell us that a previously occupied room has now become free.

# O(NlogN) time required for sorting
# O(N) creating two separate arrays of size N
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        sort_last = sorted(intervals, key = lambda k :k[1])
        sort_first = sorted(intervals, key = lambda k :k[0])

        ptr_last = 0
        ptr_first = 0

        rooms = 0
        while ptr_first < len(intervals):
            if sort_first[ptr_first][0] >= sort_last[ptr_last][1]:
                rooms -= 1
                ptr_last += 1
            ptr_first += 1
            rooms += 1
        return rooms

# Using Heap and sorted list
# O(NlogN) Sorting takes nlogn for the heap, extract-min operation on heap takes logN
# and at the worst case we need N extract-min operations
# O(N) Constructing the heap costs O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []
        sort_first = sorted(intervals, key=lambda k: k[0])
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, sort_first[0][1])

        for i in sort_first[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            # Add new room or old room with updated time
            heapq.heappush(free_rooms, i[1])
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
