from bit import wif_to_key
import os
from dotenv import load_dotenv
load_dotenv()

# access account information by accessing BTC-test private key we obtained from hd-wallet-derive command in wallet-multi.py 
# (located in keys.ipynb in btc_test_priv_keys dataframe)

key = os.getenv("WIF_KEY")

#key = PrivateKeyTestnet(key)

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

# input address we obtined from hd derive (the second BTC-test address in btc_test_keys.csv file) 
# to send funds to, send funds and obtain transaction confirmation

addresses = input(f'Please enter the address where BTC will be sent to {""}')
amount = input(f'Please enter the BTC amount to send {""}')

amount = []
addresses = []
outputs = []

print(addresses)
print(amount)

for address in addresses:
    outputs.append((address, f'{amount}', "btc"))

print(key.send(outputs))

