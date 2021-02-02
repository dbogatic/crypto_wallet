from bit import wif_to_key
import os
from dotenv import load_dotenv
load_dotenv()
from constants import * 

key = os.getenv("WIF_KEY")

key = wif_to_key(key)
print(key)

# get balance in BTC
balance = key.get_balance('btc')
print(balance)

# get balance in USD
balance_usd = key.balance_as('usd')
print(balance_usd)

# get transactions that the key participated in
tx = key.get_transactions()
print(tx)

# get Unspent Transaction Outputs (UTXOs)
unspent = key.unspents
print(unspent)

# input address to send funds to
addresses = ["n1RdWn8KdvGx9u2SxuG8Lxnvg6R7hRtDVC"]

outputs = []

for address in addresses:
    outputs.append((address, 0.000001, "btc"))

print(key.send(outputs))

