import os
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account
from pathlib import Path
from getpass import getpass
load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

account_one = Account.from_key(os.getenv("PRIVATE_KEY_SEND"))

account_two = Account.from_key(os.getenv("PRIVATE_KEY_REC"))

balance_account_one = w3.eth.getBalance(account_one.address)
balance_account_two = w3.eth.getBalance(account_two.address)


print(account_one)
print(account_one.address)
print(balance_account_one)
print(account_two)
print(account_two.address)
print(balance_account_two)

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

send_tx(account_one.address,account_two.address, 1)

