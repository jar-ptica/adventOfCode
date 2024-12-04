seads = []
k = [2, 10, 3, 5, 8, 12]
m=[]
for i in range(0, len(k), 2):
    m.append([k[i], k[i+1]])
print(m)

x = [[2, 10], [3, 5], [8, 12]]

#x =[[1,3],[2,6],[8,10],[15,18]]
def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    interval_index = 0
    #print(sorted_intervals)
    for  i in sorted_intervals:

        if i[0] > sorted_intervals[interval_index][1]:
            interval_index += 1
            sorted_intervals[interval_index] = i
        else:
            sorted_intervals[interval_index] = [sorted_intervals[interval_index][0], i[1]]
    #print(sorted_intervals)
    return sorted_intervals[:interval_index+1]

print(merge_intervals(x)) #-->[[1, 6], [8, 10], [15, 18]]
