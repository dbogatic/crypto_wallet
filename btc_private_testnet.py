from bit import PrivateKeyTestnet
from bit import wif_to_key
from bit.network import NetworkAPI, satoshi_to_currency
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


# obtain a sender's private key from keys.ipynb dataframe by selecting a specific key using iloc

btc_test_keys_df = pd.read_csv("resources/btc_test_keys")
btc_test_priv_keys = btc_test_keys_df['privkey']
btc_test_select_priv_key = btc_test_priv_keys.iloc[0]

key = PrivateKeyTestnet(btc_test_select_priv_key)

# alternatively we can read in the key from hidden .env file 

wif_key = os.getenv("WIF_KEY")
key = PrivateKeyTestnet(wif_key)

# or we could use bit 'wif_to_key' method to acomplish the same task

# from dataframe 

key = wif_to_key(btc_test_select_priv_key)

# from .env

key = wif_to_key(os.getenv("WIF_KEY"))

# print sender's address

sender = (key.address)

print(sender)

# input recipients' addresses

recipient = input(f'Please enter the address where BTC will be sent to {""}')

# input btc amount to be sent to the recipient

amount = input(f'Please enter the BTC amount to send {""}')

# obtain sender account balance in usd

''' 
Source code: https://ofek.dev/bit/guide/advanced.html

'''
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
