from datetime import date


def weekday_from_date(curr_date:date):
    return curr_date.strftime("%A").lower()