import os
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account
from pathlib import Path
load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

private_key = os.getenv("PRIVATE_KEY")
private_key2 = os.getenv("PRIVATE_ETH_KEY")
account_one = Account.privateKeyToAccount(private_key)
account_two = Account.privateKeyToAccount(private_key2)

print(account_one, account_two)

def create_raw_tx(account, recipient, amount):
    """
        Args:
            account - a w3 account object
            recipient - a W3 account object
            amount - an integer to send
    """

    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, 
        "to": recipient.address, 
        "value": amount})
    
    nonce = w3.eth.getTransactionCount(account.address)+1

    return {
        "from": account.address,
        "to": recipient.address,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": nonce
    }

def send_tx(account, recipient, amount):

    tx = create_raw_tx(account, recipient, amount)

    signed_tx = account.sign_transaction(tx)

    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    print(result.hex())

    return result.hex()


print(account_one.address)
print(account_two.address)

send_tx(account_one,account_two, 1)

