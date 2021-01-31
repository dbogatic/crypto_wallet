import subprocess
import json
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

mnemonic = os.getenv("MNEMONIC")
command = './derive -g --mnemonic --coin=ETH --numderive=3 --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)

from constants import * 

keys_df = pd.DataFrame(keys)
keys_df.to_csv("resources/eth_keys")