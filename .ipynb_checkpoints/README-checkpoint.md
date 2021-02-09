# week19_blockchain_python
In this project, we are creating a Cryptocurrency wallet to hold an unlimited number of cryptocurrencies and transact among different account addressess.

## Libraries used
Activate the virtual environment where the Web3 dependency was installed.
- os
- web3
- json
- subprocess
- eth_account

## Tools/Technologies
- Mnemonic code converter
- HD Wallet
- Github
- Gitbash
- Jupyter Lab
- Windows 10, 64-bit

## High level steps
- The function `derive_wallets()` will fetch the private, public, keys account addresses of BTCTEST and ETH, using the generated mnemonic.
- Subsequently, the above parameters will be returned in a json format.
- The function `priv_key_to_account()` will first check for the coin type and then convert the private key string in the child key to to a transactable object.
- The function `create_tx()` contains the data of unsigned transaction. Depending upon the coin type, the corresponding object is returned.
- The function `send_tx()` calls the `create_tx()` function, signs the transaction and sends it to the designated network, based on the coin type.

## Difficulties faced
- The command line code `f'./derive -g --mnemonic="{mnemonic}" --coin={coin_type} --numderive={nd} --cols=path,address,privkey,pubkey --format= json'` does not work for multiple coins, but it shows the deisred output individually.
- Even my tutor was unable to fix the problem. Thus, the project is incomplete.

## Contributors
- Satheesh Narasimman

## People who helped
- Khaled Karman, Bootcamp tutor

## References
- https://iancoleman.io/bip39/

- https://tbtc.bitaps.com/

- https://testnet-faucet.mempool.co/