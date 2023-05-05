import json

with open('clockIn.json', 'r') as f:
    data = json.load(f)

# sort the dates in descending order
sorted_data = {k: v for k, v in sorted(data.items(), reverse=True)}

with open('clockIn.json', 'w') as f:
    json.dump(sorted_data, f)
