import subprocess
import json

ETH = 'eth'
# orinigtal
# command = 'php C:/Users/Hassan/Dropbox/GithubRepo/ColumbiaFintechLab/HomeWork/hw_19_python_blockchain/wallet/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --format=json'

# try with eath
# for laptop
# command = f'php C:/Users/Hassan/Dropbox/GithubRepo/ColumbiaFintechLab/HomeWork/hw_19_python_blockchain/wallet/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --coin={ETH} --numderive=3 --format=json'

# for desktop
command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --coin={ETH} --numderive=3 --format=json'


p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err)= p.communicate()
p_status = p.wait()

# print (f'output: \n {output}')
# print (f'error: \n {err}')

keys = json.loads(output)
print(keys)
# print(keys[0][3])
