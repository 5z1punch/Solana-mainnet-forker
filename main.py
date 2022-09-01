from forker import commands, handle

from dotenv import load_dotenv

import os

load_dotenv()

if __name__ == '__main__':
    args = commands.parser().parse_args()
    attach = False
    if args.COMMAND == "start":
        attach = True
        if os.path.exists("./test-ledger"):
            print("[?] the default Ledger location `./test-ledger` exists, you can just resume it by `>> solana-test-validator` ")
            exit(0)
    forker = handle.Handle(rpc_tag=args.cluster, attach=attach, snapshoot_dir=args.snapshoot_dir, skip_builtin=not args.nskip_builtin)
    if args.extra_accounts_txt:
        forker.append_accounts(args.extra_accounts_txt)
    if args.COMMAND == "snapshoot":
        forker.snapshoot(args.tx_id)
    elif args.COMMAND == "start":
        forker.start(args.tx_id)
    