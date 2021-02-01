import subprocess
import json
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
from constants import *

# pass mnemonic phrase to derive code to obtain set of public and private keys

mnemonic = os.getenv("MNEMONIC")
command = './derive -g --mnemonic --coin=BTCTEST --numderive=3 --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

# get keys in json format
keys = json.loads(output)
print(keys)

# create dataframe with keys and print csv

keys_df = pd.DataFrame(keys)
keys_df.to_csv("resources/btc_test_keys")