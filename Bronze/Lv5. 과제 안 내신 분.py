import sys

Attendance = list(range(1, 31))

for _ in range(28):
    data = int(sys.stdin.readline())
    Attendance.remove(data)

Attendance.sort()
print(*Attendance)