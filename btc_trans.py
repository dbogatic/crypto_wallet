from bit import wif_to_key
from bit import PrivateKeyTestnet
import os
from dotenv import load_dotenv
load_dotenv()

# access account information by accessing BTC-test private key we obtained from hd derive command in wallet.py (located in keys.ipynb in btc_test_priv_keys dataframe)

key = os.getenv("WIF_KEY")

key = PrivateKeyTestnet(key)
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

# input address we obtined from hd derive (the second BTC-test address in btc_test_keys.csv file) to send funds to, send funds and obtain transaction confirmation

addresses = ["n1RdWn8KdvGx9u2SxuG8Lxnvg6R7hRtDVC"]

outputs = []

for address in addresses:
    outputs.append((address, 0.0001, "btc"))

print(key.send(outputs))

