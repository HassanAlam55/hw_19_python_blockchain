import subprocess
import json


command = 'php C:/Users/Hassan/Dropbox/GithubRepo/ColumbiaFintechLab/HomeWork/hw_19_python_blockchain/wallet/hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="barrel attack mammal crash expect note alcohol offer then worth kid current" --cols=path,address,privkey,pubkey --format=json'


p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
# print(keys[0][3])
