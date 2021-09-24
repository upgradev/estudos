total_seconds = float(input("enter a number of seconds: "))

hours = total_seconds // 3600

minutes = (total_seconds//60) % 60

seconds = total_seconds % 60

print('Hours: ', hours)
print('Minutes: ', minutes)
print("seconds: ", seconds)
