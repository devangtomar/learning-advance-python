def day_of_week(day):
    if day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    else:
        return "Other days"


def day_of_week_via_match_case(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case _:
            return "Other days"


print(day_of_week(1))
print(day_of_week_via_match_case(1))
