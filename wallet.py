import subprocess
import json
import os
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware import geth_poa_middleware
from constants import *
from eth_account import Account

load_dotenv()

w3= Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer= 0)

mnemonic= os.getenv('MNEMONIC')
account= Account.from_key(os.getenv("NODE1_PRIVATE_KEY"))

nd= 3
coins= [BTCTEST, ETH]
    
def derive_wallets():
    result = {}
    for coin_type in coins:
        commandline = f'./derive -g --mnemonic="{mnemonic}" --coin={coin_type} --numderive={nd} --cols=path,address,privkey,pubkey --format= json'
        p = subprocess.Popen(
            commandline,
            stdout=subprocess.PIPE,
            shell=True)
        output, err = p.communicate()
        p_status = p.wait()
        print(p_status)
        print(json.dumps(json.loads(output), indent=3))

        result[coin_type] = json.loads(output)
    
    return result


def priv_key_to_account (coin_type, priv_key):
    for coin_type in coins:
        if coin_type== 'ETH':
            return Account.privateKeyToAccount(priv_key)
        
        elif coin_type== 'BTCTEST':
            return PrivateKeyTestnet(priv_key)
        

def create_tx(coin_type, account, to, amount):
    gasEstimate= w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
        )
    
    for coin_type in coins:
        if coin_type== 'ETH':
            return {
                "from": account.address,
                "to": to,
                "value": amount,
                "gas": gasEstimate,
                "gasPrice":w3.eth.gasPrice,
                "nonce": w3.eth.getTransactionCount(account.address),
                "chain_id": chainID, ####
            }
        elif coin_type== 'BTCTEST':
            return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

        
def send_tx (coin_type, account, to, amount):
    for coin_type in coins:
        raw_tx= create_tx(coin_type, account, to, amount)
        signed_tx= account.sign_transaction(raw_tx)
        
        if coin_type== 'ETH':
            eth_result= w3.eth.sendRawTransaction (signed_tx.rawTransaction)
            return eth_result.hex()
        
        elif coin_type== 'BTCTEST':
            return NetworkAPI.broadcast_tx_testnet(signed_tx)