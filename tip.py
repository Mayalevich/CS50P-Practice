def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    RemoveD=d.replace("$", "")
    return float(RemoveD)


def percent_to_float(p):
    RemoveP=p.replace("%", "")
    RemoveP= float(RemoveP)/100
    return RemoveP



main()
