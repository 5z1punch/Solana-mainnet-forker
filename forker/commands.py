import argparse

def parser():
    parser = argparse.ArgumentParser(description='Fork accounts from mainnet/devnet on-demand.')
    parser.add_argument('--url', '-u', metavar='mainnet/devnet/rpc_url', dest='cluster', default='mainnet',
                        help='fork from mainnet or devnet or a rpc url starts with `http://` or `https://` ')
    parser.add_argument('--tx', '-t', dest='tx_id', 
                        help='fork all accounts associated with the tx id')
    parser.add_argument('--nskip-builtin', dest='nskip_builtin', action='store_true',
                        help='Do NOT skip built-in accounts of the solana. Default skip.')
    parser.add_argument('--snapshoot-dir', '-s', dest='snapshoot_dir', default='./snapshoot',
                        help='snapshoot dir to save and load.')
    parser.add_argument('--extra-accounts', '-e',  metavar='extra-accounts.txt', dest='extra_accounts_txt', default=None,
                        help='add extra accounts to snapshoot from a line by line file')
    # parser.add_argument('--check-exist', dest='check_exist', action='store_true',
    #                     help='Force check if the account exists, PDA or closed Accounts will be printed and filtered. Default false. ')
    parser.add_argument('COMMAND', metavar='COMMAND', choices=['snapshoot', 'start'],
                        help='snapshoot / start')
    
    snapshoot_group = parser.add_argument_group('snapshoot', 'Only snapshoot the accounts and save to disk.')
    start_group = parser.add_argument_group('start', 'run solana-test-validator with forked accounts.')
    return parser

if __name__ == '__main__':
    parser = parser()
    args = parser.parse_args()
