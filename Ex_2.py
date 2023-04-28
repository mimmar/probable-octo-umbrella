'''
day = int(input('Enter the day you dropped your shoes off? (Monday=1, Sunday=7): '))
duration = int(input('how long does the repair take?: '))


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_sans_sunday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

pick_up = days % 7

if days[pick_up] != "Sunday":
    return_day = days[pick_up]
else:
    pick_up = days_sans_sunday[0]

print(f'The shoes will be ready for pick up on: {pick_up}')
'''
'''
day = int(input("What day of the week did you leave your shoes for repair? (Monday=1, Sunday=7): "))
duration = int(input("How many days will the repair take? "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_sans_sunday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

when = (day - 1 + duration) % 7

if days[when] == "Sunday":
    continue
else:
    return_day = days[when]

print(f'You can pick up your shoes on {return_day}')
'''
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_sans_sunday = days[0:6]

day_of_week = int(input("What day of the week did you leave your shoes for repair? (Monday=1, Sunday=7): "))
repair_days = int(input("How many days will the repair take? "))

pick_up_day = day_of_week - 1  # adjust for 0-based indexing

for i in range(repair_days):
    pick_up_day += 1
    if pick_up_day == 6:  # skip Sunday
        pick_up_day += 1
        continue
    elif pick_up_day > 6:
        pick_up_day = 0

return_day: str = days[pick_up_day]

print(f'You can pick up your shoes on a {return_day}')