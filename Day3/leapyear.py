year = int(input("Which year do you want to check? "))
year_by_4 = year % 4
year_by_100 = year % 100
year_by_400 = year % 400
if year_by_4 == 0:
    print(f"{year_by_4} divisible by 4")
    if year_by_100 == 0:
        print(f"{year_by_4} divisible by 100")
        if year_by_400 == 0:
            print(f"{year_by_4} divisible by 400")
            print("Leap year.")
        else:
            print(f"{year_by_4} not divisible by 400")
            print("Not leap year.")
    else:
        print(f"{year_by_4} not divisible by 100")
        print("Leap year.")
else:
    print(f"{year_by_4} not divisible by 4")
    print("Not leap year.")
