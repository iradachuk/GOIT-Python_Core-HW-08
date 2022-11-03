from datetime import datetime, timedelta

birthday_list = [ 
    {'name': 'Ivan', 'birthday': datetime(1997, 11, 14)}, # Monday
    {'name': 'Petro', 'birthday': datetime(1999, 11, 6)}, # Sunday
    {'name': 'Anna', 'birthday': datetime(1999, 11, 7)}, # Monday
    {'name': 'Anton', 'birthday': datetime(1999, 11, 8)}, # Tuesday
    {'name': 'Olena', 'birthday': datetime(1999, 11, 10)} # Thursday
    ]


def get_birthdays_per_week(users):
    birthdays_per_week = {}
    current_date = datetime.now()
    start = current_date + timedelta(days=1)
    end = start + timedelta(days=6)

    week_days = {
        0: 'Monday',
        1: 'Tuesday', 
        2: 'Wednesday', 
        3: 'Thursday', 
        4: 'Friday', 
        5: 'Saturday', 
        6: 'Sunday'
        }
    
    for user in users:
        user['birthday'] = user['birthday'].replace(year=current_date.year)

        if start < user['birthday'] < end:
            d_name = week_days.get(user['birthday'].weekday())

            if d_name == 'Saturday' or d_name == 'Sunday':
                d_name = 'Monday'

            if d_name not in birthdays_per_week:
                birthdays_per_week[d_name] = []
            birthdays_per_week[d_name].append(user['name'])

    for day in week_days.values():
        if day in birthdays_per_week.keys():
            t = ', '.join(birthdays_per_week[day])
            print(f'{day}: {t}')    



if __name__ == '__main__':
    get_birthdays_per_week(birthday_list)