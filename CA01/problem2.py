#CA01 Problem2

# Write a program which converts all units of time into seconds.
# Sample input: "3 days, 14 hours, 27 minutes, 33 seconds.
# Sample output: 311253 seconds

time = input("Please enter: Days, Hours, Minutes, Seconds: ")

parts = time.split(",")  # Split by comma
days = int(parts[0].split()[0])       # Extract the number before 'days'
hours = int(parts[1].split()[0])      # Extract the number before 'hours'
minutes = int(parts[2].split()[0])    # Extract the number before 'minutes'
seconds = int(parts[3].split()[0])    # Extract the number before 'seconds'


time = days, hours, minutes, seconds  

days_in_seconds = days * 24 * 60 * 60
hours_in_seconds = hours * 60 * 60
minutes_in_seconds = minutes * 60

result = days_in_seconds + hours_in_seconds + minutes_in_seconds + seconds

print(f"\n{result} seconds.")