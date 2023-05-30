import requests
import json
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

bitcoin = response.json()
bit_value = (bitcoin["bpi"]["USD"]["rate"])



try:
    quantity = float(sys.argv[1])
    bit_value = str(bit_value)
    bit_value = bit_value.replace(",","")
    bit_value = float(bit_value)



    total = quantity*bit_value
    print(f"${total:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("something went wrong")




















#bitcoin = json.dumps(response.json(), indent = 2)