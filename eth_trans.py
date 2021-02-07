import os
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account
from pathlib import Path
from getpass import getpass
load_dotenv()


# we will be using a Web3 library on a local host to conduct eth transaction between two nodes in a running local blockchain "bogicash"

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# obtain sender eth address by using a private key. 'privateKeytoAccount' method is being deprecated for 'Account.from' method, which was used here.
# The keys are created using hd-wallet-derive and can be seen in eth_keys.csv or keys.ipynb

account_one = Account().from_key(os.getenv("PRIVATE_KEY_SEND"))

# input the address where ETH will be sent 

account_two = input(f'Please type in the address where ETH will be sent to {""}')

# obtain account balance for the sender and reciever 

balance_account_one = w3.eth.getBalance(account_one.address)
balance_account_two = w3.eth.getBalance(account_two)

# print accounts, addresses and balances for sender and receiver 

print(account_one)
print(account_one.address)
print(balance_account_one)
print(account_two)
print(account_two)
print(balance_account_two)

# define, create and confirm a ETH transaction from sender to receiver and estimate gas (miner) fees. 
# Nonce + 1 is to ensure transactions are not being canceled because of the same nonce value

def create_raw_tx(sender, recipient, amount):

    gasEstimate = w3.eth.estimateGas(
        {"from": sender, 
        "to": recipient, 
        "value": amount})
    
    nonce =  w3.eth.getTransactionCount(sender)+1

    return {
        "from": sender,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": nonce
    }


def send_tx(sender, recipient, amount):

    tx = create_raw_tx(sender, recipient, amount)

    signed = account_one.sign_transaction(tx)

    print("signed",signed.rawTransaction)

    result = w3.eth.sendRawTransaction(signed.rawTransaction)

    print(result.hex())

    return result.hex()

# send ETH transaction after entering the amount in input prompt; wait for the confirmation

send_tx(account_one.address,account_two, int(input('Input ETH amount to be sent (do not enter float): ')))
