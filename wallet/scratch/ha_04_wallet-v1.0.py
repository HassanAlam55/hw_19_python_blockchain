import subprocess
import json

# path to hd-wallet-derive for me is: 
# /home/jwales/bootcamp/cryptostuff/hd-wallet-derive/hd-wallet-derive.php

# command = '/home/jwales/bootcamp/cryptostuff/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --format=json'
# command = 'C:/Users/Hassan/Dropbox/GithubRepo/ColumbiaFintechLab/HomeWork/hw_19_python_blockchain/wallet/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --format=json'

command = 'php C:/Users/Hassan/Dropbox/GithubRepo/ColumbiaFintechLab/HomeWork/hw_19_python_blockchain/wallet/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --format=json'

# .\hd-wallet-derive\hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --format=json

# PS C:\Users\Hassan\Dropbox\GithubRepo\ColumbiaFintechLab\HomeWork\hw_19_python_blockchain\wallet>

# C:\Users\Hassan\Dropbox\GithubRepo\ColumbiaFintechLab\HomeWork\hw_19_python_blockchain\wallet\hd-wallet-derive\hd-wallet-derive.php
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
#keys[0].privkey
