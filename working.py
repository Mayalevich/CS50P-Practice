def main():
    print(convert(input("Hours: ")))

def convert(s):
    result = ""
    times = s.split(" to ")
    if len(times) != 2:
        raise ValueError("Input does not contain exactly two times separated by 'to'")

    start_time = times[0]
    end_time = times[1]

    start_24 = convert_time_to_24(start_time)
    end_24 = convert_time_to_24(end_time)

    result += start_24
    result += " to "
    result += end_24

    return result

def convert_time_to_24(time_str):
    am_pm = ["AM", "PM"]
    for period in am_pm:
        if period in time_str:
            time_period = period
            break
    else:
        raise ValueError("Invalid time format: Missing AM or PM")

    time_components = time_str.split(" ")

    if len(time_components) != 2:
        raise ValueError("Invalid time format")

    time = time_components[0]
    period = time_components[1]

    if ":" in time:
        hours, minutes = time.split(":")
    else:
        hours = time
        minutes = "00"

    hours = int(hours)
    minutes = int(minutes)

    if hours < 1 or hours > 12 or minutes < 0 or minutes > 59:
        raise ValueError("Invalid time value")

    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours += 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
