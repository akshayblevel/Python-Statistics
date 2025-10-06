data = [14, 10, 81, 17, 10, 17, 16, 11, 84]

def mode(data):
   """Calculates the mode(s) of a list of numbers."""
   counts = {}
   for item in data:
       counts[item] = counts.get(item, 0) + 1
   max_count = max(counts.values())
   return [item for item, count in counts.items() if count == max_count]

print("Mode: ",mode(data))