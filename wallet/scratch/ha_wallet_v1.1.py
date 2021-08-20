# Import dependencies
import subprocess
import json
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
 
 
# Create a function called `derive_wallets`
def derive_wallets(Mnemonic, Coin, Numderive, Format  ):
#     command = # YOUR CODE HERE
    command = f'php C:/Users/Hassan/Dropbox/GithubRepo/ColumbiaFintechLab/HomeWork/hw_19_python_blockchain/wallet/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic=Mnemonic --cols=path,address,privkey,pubkey --coin={Coin} --numderive=Numderive --format=Format'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = # YOUR CODE HERE

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    # YOUR CODE HERE
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)# what is account
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
        
    else:
        return ('error')
        

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, recipient, amount):
    # YOUR CODE HERE
    if coin == ETH:
       # need to fix parameters
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
            )
        return {
            "from": account.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            }
    
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    else:
        return ('error')
        
    

    
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, recipient, amount):
    if coin == ETH:
    # YOUR CODE HERE
        tx = create_tx(account, recipient, amount)
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
#     print(result.hex())
        return result

    if coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed)
    else:
        return ('error')
        

