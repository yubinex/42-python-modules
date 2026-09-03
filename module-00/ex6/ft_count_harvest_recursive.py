def count_day(current_day, final_day):
    if current_day > final_day:
        return
    print(f"Day {current_day}")
    count_day(current_day + 1, final_day)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    count_day(1, days)
    print("Harvest time!")
