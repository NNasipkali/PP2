#1 
from datetime import datetime, timedelta

now = datetime.now()
new_date = now - timedelta(days = 5)

print("Current date:", now)
print("5 days ago:", new_date)

#2 
from datetime import datetime, timedelta

now = datetime.now()

tomorrow = now + timedelta(days= 1)
yesterday = now - timedelta(days= 1)

print("Yesterdar:", yesterday)
print("Today:", now)
print("Tomorrow:", tomorrow)

#3 
from datetime import datetime, timedelta

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", no_microseconds)

#4
from datetime import datetime

date1 = datetime(2026, 2, 10, 12, 0, 0)
date2 = datetime(2026, 2, 19, 12, 0, 0)

difference = date2 - date1

print("Difference:", difference)
print("Difference in seconds:", difference.total_seconds())
