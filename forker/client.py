import base64
import base58

from solana.rpc.api import Client as apiClient
from solana.keypair import Keypair
import solders.keypair

from . import constant

class Client:
    def __init__(self, rpc_url, kp_file=None) -> None:
        self.rpc_client = apiClient(rpc_url)
        if kp_file:
            with open(kp_file) as kp_file_handle:
                s_kp = solders.keypair.Keypair.from_json(kp_file_handle.read())
                self.signer = Keypair.from_solders(s_kp)
        else:
            self.signer = None
            print("[*] not load a signer keypair.")
    
    def get_tx_input_accounts(self, tx_id):
        transaction = self.rpc_client.get_transaction(tx_id)
        account_keys = transaction["result"]["transaction"]["message"]["accountKeys"]
        return account_keys

    def get_accounts(self, account_pubkeys, skip_builtin=True):
        input_accounts = []
        for address in account_pubkeys:
            if address in constant.RUNTIME_FACILITIES and skip_builtin:
                print(f"[*] account {address} is a solana builtin account ")
                continue
            print(f"[*] loading account {address}")
            resp = self.rpc_client.get_account_info(address)
            if resp["result"]["value"]:
                input_accounts.append({"pubkey": address, "account":resp["result"]["value"]})
            else:
                print(f"[!!!] account {address} cant be found, its maybe a PDA or closed token account" )
        return input_accounts
    
    def get_bpf_account(self, program_account):
        data_p = program_account["account"]["data"]
        assert data_p[1] == "base64" # 默认使用 base64 
        data = base64.b64decode(data_p[0])
        exec_data_account = base58.b58encode(data[4:]).decode()
        print(f"[*] loading Executable Data Account {exec_data_account} of program {program_account['pubkey']}")
        resp = self.rpc_client.get_account_info(exec_data_account)
        if resp.get('error') or not resp.get("result") or not resp["result"].get("value"):
            print(f"[!] Executable Data Account cant be found, maybe a builtin program")
            return None
        return {"pubkey": exec_data_account, "account":resp["result"]["value"]}
        
