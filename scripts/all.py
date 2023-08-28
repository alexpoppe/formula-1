import os

print("\n=================\n")
print("calculating the optimal calendar")
os.system("python scripts/optimal_calendar.py")

print("\n=================\n")
print("calculating the calendar with 1 hub")
os.system("python scripts/hubs.py 1")

print("\n=================\n")
print("calculating the calendar with 2 hubs")
os.system("python scripts/hubs.py 2")

print("\n=================\n")
print("calculating the calendar with 3 hubs")
os.system("python scripts/hubs.py 3")

print("\n=================\n")