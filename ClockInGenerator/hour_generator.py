import random
from datetime import datetime, timedelta

entry1 = (datetime.now().replace(hour=8, minute=1) + timedelta(minutes=random.randint(0, 39)))
exit1 = (datetime.now().replace(hour=12, minute=1) + timedelta(minutes=random.randint(0, 14)))
entry2 = (exit1 + timedelta(minutes=60)) + timedelta(minutes=random.randint(1, 14))
exit2 = (entry2 + timedelta(minutes=(480 - int(((exit1 - entry1).total_seconds()) / 60))))

print(f'Entry 1: {entry1.strftime("%H:%M")}\n',
      f'Exit 1: {exit1.strftime("%H:%M")}\n',
      f'Entry 2: {entry2.strftime("%H:%M")}\n',
      f'Exit 2: {exit2.strftime("%H:%M")}')
