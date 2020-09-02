'''Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed 
ranges.Meeting is represented as a list having tuples in form of (start time , end time)'''

# Time complexity is O(nlogn)

def merge_meetings_time(meetinglist):

    # Sort the meetings by start time
    meetings_sorted = sorted(meetinglist)
    
    # Initialize with the first element of meetings_sorted
    merged_meetings = [meetings_sorted[0]]
    
    for current_meeting_start , current_meeting_end in meetings_sorted[1:]:
        last_merged_meeting_start , last_merged_meeting_end = merged_meetings[-1] #Last merged will always be the last item in list

        # First case: Where the two meetings overlap
        if current_meeting_start <= last_merged_meeting_end: 
            print('Merger  done between', (current_meeting_start , current_meeting_end) ,'and' ,(last_merged_meeting_start , last_merged_meeting_end))
            merged_meetings[-1] = (last_merged_meeting_start , max(current_meeting_end ,last_merged_meeting_end))
        
        else: # If they don't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end)) 
    
    return merged_meetings

sample_input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print('Given schedule is  :', sample_input)
print('After compaction the schedule is : ', end = '')
print(merge_meetings_time(sample_input))