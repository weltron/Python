import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing commmand-line argument")
else:
    try:
        amount = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = response.json()
    total = result["bpi"]["USD"]["rate_float"] * amount
    print(f"${total:,.4f}")
except requests.RequestException:
    pass
