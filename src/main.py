def max_meetings(start, finish):
    n = len(start)
    meetings = list(zip(start, finish, range(1, n + 1)))
    meetings.sort(key=lambda x: x[1])

    selected = []
    last_finish = 0

    for s, f, idx in meetings:
        if s > last_finish:
            selected.append(idx)
            last_finish = f

    return selected


# --- Verification with Sample Input 1 ---
s1 = [1, 3, 0, 5, 8, 5]
f1 = [2, 4, 6, 7, 9, 9]
print("Selected Meetings (Sample 1):", max_meetings(s1, f1))
# Expected Output: [1, 2, 4, 5]

# --- Verification with Sample Input 2 ---
s2 = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
f2 = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
print("Selected Meetings (Sample 2):", max_meetings(s2, f2))
# Expected Output: [6, 7, 1]