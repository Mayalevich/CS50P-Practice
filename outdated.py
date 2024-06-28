months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        # Handle numeric format MM/DD/YYYY
        if '/' in date:
            month, day, year = date.split('/')
            month, day, year = int(month), int(day), int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        # Handle written format Month DD, YYYY
        else:
            month_str, day, year = date.replace(",", "").split()
            if month_str in months:
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)
                if 1 <= day <= 31:
                    break
    except (ValueError, IndexError):
        pass

    print()

print(f"{year}-{month:02}-{day:02}")
