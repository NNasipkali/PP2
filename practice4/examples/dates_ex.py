from datetime import datetime, timedelta

# Example 1

now = datetime.now()
print("Current date and time:", now)

# Example 2

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

# Example 3

date1 = datetime(2025, 3, 1)
date2 = datetime(2026, 3, 1)

difference = date2 - date1
print("Difference in days:", difference.days)