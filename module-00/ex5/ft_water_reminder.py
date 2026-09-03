def ft_water_reminder() -> None:
    num_days = int(input("Days since last watering: "))
    if num_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
