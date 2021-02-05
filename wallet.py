import subprocess
import json
from pprint import pprint
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
from constants import *

# input coin code for BTC-test, ETH or BTC after the prompt to obtain keys for the selected crypto

which_coin = input(f" Which coin? Type in one of the following: {BTCTEST, BTC, ETH}")

print(which_coin)

# pass mnemonic phrase to derive code to obtain set of public and private keys

mnemonic_phrase = os.getenv("MNEMONIC")

# pass the command to derive keys for eth and btc-test

command = f" ./derive -g  --mnemonic='{mnemonic_phrase}' --coin='{which_coin}' --numderive=3  --cols=path,address,privkey,pubkey --format=json "

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

# get keys in json format
keys = json.loads(output)
print(keys)

# create dataframe with keys and print json

keys_df = pd.DataFrame(keys)
keys_df.to_csv("resources/eth_keys")