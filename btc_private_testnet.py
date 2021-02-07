from bit import PrivateKeyTestnet
from bit.network import NetworkAPI, satoshi_to_currency
import os
from dotenv import load_dotenv
load_dotenv()


# obtain a sender's private key

key = os.getenv('WIF_KEY')
key = PrivateKeyTestnet(key)

# print sender's address

sender = (key.address)

print(sender)

# input recipients' addresses

recipient = input(f'Please enter the address where BTC will be sent to {""}')

# input btc amount to be sent to the recipient

amount = input(f'Please enter the BTC amount to send {""}')

# obtain sender account balance in usd

btc_balance_usd = satoshi_to_currency(NetworkAPI.get_balance_testnet(f"{sender}"), 'usd')

print(btc_balance_usd)

# obtain sender account balance in btc

btc_balance_btc = satoshi_to_currency(NetworkAPI.get_balance_testnet(f"{sender}"), 'btc')

print(btc_balance_btc)

# prepare btc transaction

tx_data = key.prepare_transaction(f"{sender}",[(f"{recipient}", f"{amount}",'btc')])

print(tx_data)

# sign btc transaction

tx_hex = key.sign_transaction(tx_data)
print(tx_hex)

# send btc transaction and obtain tx confirmation

tx_hash = key.send([(f"{recipient}",f"{amount}",'btc')])

# print transaction confoirmation

print(tx_hash)
