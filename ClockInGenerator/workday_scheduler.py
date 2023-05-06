import datetime
from dateutil import parser
from shift_generator import Workday
from file_handler import JSONFileHandler

# Create an instance of JSONFileHandler with the file path
file_handler = JSONFileHandler('employee_work_hours.json')

# Load data from the JSON file
data = file_handler.load_data()

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

# Create times for the working days
current_date = most_recent_date
while working_days > 0:
    current_date += datetime.timedelta(days=1)
    if current_date.weekday() < 5:  # If the current date is a weekday
        workday = Workday()
        workday.generate_shifts()
        working_days -= 1
        date_str = current_date.strftime('%m/%d')
        data[date_str] = {
            'input01': workday.shift1.start_time.strftime('%H:%M'),
            'exit01': workday.shift1.end_time.strftime('%H:%M'),
            'input02': workday.shift2.start_time.strftime('%H:%M'),
            'exit02': workday.shift2.end_time.strftime('%H:%M'),
        }

# Sort the dates in descending order
data = {k: v for k, v in sorted(data.items(), reverse=True)}

# Write updated data back to file
file_handler.write_data(data)