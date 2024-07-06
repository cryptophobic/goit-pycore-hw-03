from datetime import datetime, timedelta


def get_upcoming_birthdays(users_to_check):
    greetings_list = []
    today = datetime.today().date()
    for user in users_to_check:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        greetings_day = datetime(today.year, birthday.month, birthday.day).date()

        if today > greetings_day:
            continue

        if greetings_day < birthday:
            continue

        if greetings_day - today <= timedelta(days=7):
            if greetings_day.weekday() > 4:
                greetings_day = greetings_day + timedelta(days=7 - greetings_day.weekday())

            greetings_list.append({'name': user['name'], 'congratulation_date': greetings_day.strftime("%Y.%m.%d")})

    return greetings_list


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
