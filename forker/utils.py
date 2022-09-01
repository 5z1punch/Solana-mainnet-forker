import json
import os

def save_account(account, save_dir):
    with open(os.path.join(save_dir, account["pubkey"]+".json"), 'w') as j:
        json.dump(account, j)