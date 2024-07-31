import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')

    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    data = data.json()
    rate = data["bpi"]["USD"]["rate_float"]
    total = number * rate
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
