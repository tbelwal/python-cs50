# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
# Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.
import sys
import requests
import json


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif not float(sys.argv[1]):
        sys.exit("Command-line argument is not a number")

    amount = float(sys.argv[1]) * float(get_price())

    print(f"${amount:,.4f}")


def get_price():
    api_key = "ca7666702b81e6b9fb5241f53dba497cf14e77d58fe5636acf705e18e43b4476"

    try:
        url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api_key
    except requests.exceptions.HTTPError as http_err:
        # Catches 404, 500, etc.
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        # Catches DNS failures, refused connections
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as time_err:
        # Catches connect and read timeouts
        print(f"Timeout error occurred: {time_err}")
    except requests.exceptions.RequestException as general_err:
        # Catches any other requests-related exception
        print(f"An unexpected requests error occurred: {general_err}")

    response = requests.get(url)
    data = response.json()

    return data["data"]["priceUsd"]


if __name__ == "__main__":
    main()
