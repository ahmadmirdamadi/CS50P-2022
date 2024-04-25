import sys
import requests


if len(sys.argv) == 2:
    try:
        v = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    res = r.json()
    bit = res['bpi']['USD']['rate_float']
    ta = bit * v
    print(f"${ta:,.4f}")

except requests.RequestException:
    print("request exception sodi!!")
    sys.exit(1)