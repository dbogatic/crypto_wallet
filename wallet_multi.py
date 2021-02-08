import subprocess
import json
from pprint import pprint
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
from constants import *

# input coin code for BTC-test, ETH or BTC after the prompt to obtain keys for the selected 
# crypto to initiate transactions from the imported py transaction files 

which_coin = input(f" Select your coin to obtain a private key. Type in one of the following: {BTCTEST, BTC, ETH}")

''' 
Source code: https://stackoverflow.com/questions/32928143/how-to-continue-asking-user-for-input-until-it-is-considered-valid

'''

# ask user for the correct input if incorrect one provided; if correct input derive keys and initiate a crypto transaction

while which_coin not in ("btc-test", "eth", "btc"):
    
    print(f"This is not a valid entry, please pick again from {BTCTEST, BTC, ETH}.")
    
    which_coin = input(f" Select your coin to obtain a private key. Type in one of the following: {BTCTEST, BTC, ETH}")

print(f"Thank you! Here are your {which_coin} keys and transaction!")

# pass mnemonic phrase to derive code to obtain set of public and private keys

mnemonic_phrase = os.getenv("MNEMONIC")

# pass the command to derive keys for eth and btc-test

command = f" ./derive -g  --mnemonic='{mnemonic_phrase}' --coin='{which_coin}' --numderive=3  --cols=path,address,privkey,pubkey --format=json "

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

# get keys in json format
keys = json.loads(output)

# create dataframe with keys 

keys_df = pd.DataFrame(keys)

# print keys to .csv file if needed

#keys_df.to_csv("resources/eth_keys")

print(keys)

# pass the appropriate py file based on coin selection to obtain sender's private keys, 
# verify addresses, balances and execute transactions and see confirnmations; follow the 
# user input prompts to enter recipient addresses and amounts to be sent 
    
if f'{which_coin}' == 'btc-test':
    import btc_private_testnet
    print(btc_private_testnet)
    
elif f'{which_coin}' == 'eth':
    import eth_trans
    print(eth_trans)
     
else: pass
