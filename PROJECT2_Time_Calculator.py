# PROJECT 2: TIME CALCULATOR



DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def add_time(start, duration, day=""):
    calculated_days = 0
    duration_time_index = duration.index(':')
    total_hours_duration = int(duration[:duration_time_index])
    mins_left = int(duration[duration_time_index+1:])
    calculated_days += total_hours_duration // 24
    hours_left = total_hours_duration - calculated_days*24

    start_time_index1 = start.index(':')
    start_time_index2 = start.index(' ')
    total_mins = int(start[start_time_index1+1:start_time_index2]) + mins_left
    actual_mins = total_mins % 60
    hour_remainder = total_mins // 60
    total_hour = int(start[:start_time_index1]) + hours_left + hour_remainder
    actual_hour = total_hour % 12

    meridian = start[start_time_index2+1:]
    next_day = ""
    new_day = ""
    if actual_hour != total_hour:
        if meridian == 'PM':
            meridian = "AM"
            calculated_days += 1
        else:
            meridian = "PM"
    if calculated_days == 1:
        next_day = " (next day)"
    elif calculated_days > 1:
        next_day = f" ({calculated_days} days later)"
    if day:
        day_index = DAYS.index(day.lower())
        new_day_index = (day_index + calculated_days) % 7
        new_day = ", "+DAYS[new_day_index].capitalize()

    return f"{'12' if actual_hour==0 else actual_hour}:{'0' if actual_mins< 10 else ''}{actual_mins} {meridian}{new_day}{next_day}"



print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)









