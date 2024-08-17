from datetime import date
import inflect
import sys

def main():
    birth_date = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date format")

    today = date.today()
    minutes = calculate_minutes(birth_date, today)
    print(f"{convert_to_words(minutes)} minutes")

def calculate_minutes(birth_date, today):
    delta = today - birth_date
    return delta.days * 24 * 60

def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()
