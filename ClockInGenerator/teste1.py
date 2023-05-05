import datetime
import json
from dateutil import parser

# Load data from the clockIn.json file
with open("clockIn.json", "r") as file:
    data = json.load(file)

# Get the keys (dates) from the data dictionary and parse them as datetime objects
dates = [parser.parse(date) for date in data.keys()]

# Get the most recent date from the data
most_recent_date = max(dates)

# Check if today is a weekday (Monday - Friday)
today = datetime.datetime.today()
if today.weekday() >= 5:  # If today is Saturday or Sunday
    days_to_subtract = today.weekday() - 4  # Subtract days to get to Friday
    today = today - datetime.timedelta(days=days_to_subtract)  # Set today to Friday

# Calculate the difference in working days between the most recent date and today
working_days = 0
current_date = most_recent_date
while current_date.date() != today.date():
    current_date += datetime.timedelta(days=1)
    if current_date.weekday() < 5:  # If the current date is a weekday
        working_days += 1

print(f"The difference in working days is {working_days} days")
