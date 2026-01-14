from datetime import date, timedelta

print('Time-index task knowledge system: ')

#task
task = ["task" + str(X) for X in range(1, 4)]

#stream
stream = {"stream A":"RMP", "stream B":"PWN", "stream C":"O"}

#day
def day(start = date(2026,1,15), end = date(2026,1,16)):
    current = start
    while current <= end:
        print("Date:", current)
        for i in stream:
            print("\n", stream[i], "\n", task)
        current += timedelta(days=1)

for d in day(start = date(2026,1,15), end = date(2026,1,16)):
    print(d)



