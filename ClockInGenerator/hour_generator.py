import random
from datetime import datetime, timedelta

class Shift:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = (end_time - start_time).total_seconds() / 60
        
class Workday:
    def __init__(self):
        self.shift1 = None
        self.shift2 = None
    
    def generate_shifts(self):
        start_time1 = datetime.now().replace(hour=8, minute=1) + timedelta(minutes=random.randint(0, 39))
        end_time1 = datetime.now().replace(hour=12, minute=1) + timedelta(minutes=random.randint(0, 14))
        start_time2 = end_time1 + timedelta(minutes=60) + timedelta(minutes=random.randint(1, 14))
        end_time2 = start_time2 + timedelta(minutes=480 - int((end_time1 - start_time1).total_seconds() / 60))
        
        self.shift1 = Shift(start_time1, end_time1)
        self.shift2 = Shift(start_time2, end_time2)
            
if __name__ == '__main__':
      workday = Workday()
      workday.generate_shifts()
# print(workday.shift1.start_time.strftime("%H:%M"))
# print(workday.shift1.end_time.strftime("%H:%M"))
# print(workday.shift2.start_time.strftime("%H:%M"))
# print(workday.shift2.end_time.strftime("%H:%M"))
