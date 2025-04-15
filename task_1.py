data = '1h 45m,360s,25m,30m 120s,2h 60s'
time_parts = data.split(',')
total_minutes = 0

for item in time_parts:
    parts = item.split()  # Разделяем каждую часть по пробелу
    for time in parts:    # Проходим по каждому кусочку: '1h', '45m' и т.п.
        if 'h' in time:
            total_minutes += int(time.replace('h', '')) * 60
        elif 'm' in time:
            total_minutes += int(time.replace('m', ''))
        elif 's' in time:
            total_minutes += int(time.replace('s', '')) // 60

print(total_minutes)
