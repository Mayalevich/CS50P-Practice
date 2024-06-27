def main():
    a = input("time: ")
    time = convert(a)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(a):
    hours, minutes = a.split(":")
    minutes = float(minutes) / 60
    return float(hours) + minutes

if __name__ == "__main__":
    main()
