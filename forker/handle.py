import os
from datetime import date
import subprocess

from .client import Client
from . import utils

class Handle:

    def __init__(self, rpc_tag, attach, snapshoot_dir='./snapshoot', skip_builtin=True) -> None:
        if rpc_tag.lower() == "mainnet":
            self.rpc_url = os.getenv("MAINNET_RPC")
            self.rpc_tag = "mainnet-beta"
        elif rpc_tag.lower() == "devnet":
            self.rpc_url = os.getenv("DEVNET_RPC")
            self.rcp_tag = "devnet"
        elif rpc_tag.startswith("http://") or rpc_tag.startswith("https://"):
            self.rpc_url = rpc_tag
            self.rpc_tag = rpc_tag
        else:
            raise Exception("invalid rpc url")

        self.client = Client(self.rpc_url)

        self.save_dir = snapshoot_dir
        self.skip_snapshoot = False
        if os.path.exists(self.save_dir):
            if not attach:
                today = date.today()
                self.save_dir += "-" + today.strftime("%Y-%m-%d")
            else:
                self.skip_snapshoot = True
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)

        self.skip_builtin = skip_builtin
        self.extra_accounts = set()

    def append_accounts(self, accounts_txt):
        with open(accounts_txt) as f:
            for l in f:
                self.extra_accounts.add(l.strip())
    
    def snapshoot(self, tx_id):
        input_accounts_keys = set(self.client.get_tx_input_accounts(tx_id))
        input_accounts_keys.update(self.extra_accounts)
        input_accounts = self.client.get_accounts(list(input_accounts_keys), self.skip_builtin)
        for account in input_accounts:
            utils.save_account(account, self.save_dir)
            if account["account"]["executable"]:
                account_info = self.client.get_bpf_account(account)
                if account_info:
                    utils.save_account(account_info, self.save_dir)

    def start(self, tx_id):
        if not self.skip_snapshoot:
            self.snapshoot(tx_id)
        process_args = ["solana-test-validator","-u", self.rpc_tag]
        for fname in os.listdir(self.save_dir):
            if not fname.endswith(".json"):
                continue
            _tmp_args = ["--account", fname[:-5], os.path.join(self.save_dir, fname)]
            process_args.extend(_tmp_args)
        subprocess.run(process_args)
