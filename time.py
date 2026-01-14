#print a timeline
print("Time-index task knowledge system: ")
#nested data structure: list TIMELINE chứa dictionary DAY chứa dictionary STREAM chứa list PROGRAM
stream = {"Stream" + str(X): ["pro1", "pro2"] for X in range(1, 4)}
stream2 = {"Stream" + str(X): ["pro1", "pro2"] for X in range(1, 4)}
day = {"Day" + str(X): stream for X in range(1, 3)}
# day1 = ["Stream" + str(X) for X in range(1, 4)]
# day2 = ["Stream" + str(X) for X in range(1, 4)]
timeline = [
    day
]
print (timeline)

#nếu là dictionary thì phải dùng : thay vì = trong khai báo