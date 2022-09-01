# https://github.com/solana-labs/solana/tree/master/docs/src/developing/runtime-facilities
# https://github.com/solana-labs/solana/blob/master/explorer/src/utils/tx.ts

RUNTIME_FACILITIES = [
    "SysvarC1ock11111111111111111111111111111111", 
    "SysvarEpochSchedu1e111111111111111111111111", 
    "SysvarFees111111111111111111111111111111111", 
    "Sysvar1nstructions1111111111111111111111111", 
    "SysvarRecentB1ockHashes11111111111111111111", 
    "SysvarRent111111111111111111111111111111111", 
    "SysvarS1otHashes111111111111111111111111111", 
    "SysvarS1otHistory11111111111111111111111111", 
    "SysvarStakeHistory1111111111111111111111111",
    "SysvarRewards111111111111111111111111111111",  # ←↑-- sysvars

    "11111111111111111111111111111111", 
    "Config1111111111111111111111111111111111111", 
    "Stake11111111111111111111111111111111111111", 
    "Vote111111111111111111111111111111111111111", 
    "BPFLoaderUpgradeab1e11111111111111111111111", 
    "Ed25519SigVerify111111111111111111111111111", 
    "KeccakSecp256k11111111111111111111111111111",   # ←↑-- programs

    "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL", 
    "Feat1YXHhH6t1juaWF74WLcfv4XoNocjXA6sPWHNgAse", 
    "LendZqTs7gn5CTSJU1jWKhKuVpjJGom45nnwPb2AMTi", 
    "Memo1UhkJRfHyvLMcVucJwxXeuD728EqVDDwQDxFMNo", 
    "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr", 
    "namesLPneVptA9Z5rqUDD9tMTWEJwofgaYwp8cawRkX", 
    "SPoo1Ku8WFXoNDMHPsrGSTSG1Y47rzgn41SLUNakuHy", 
    "SwaPpA9LAaLfeLi3a68M4DjnLqgtticKg6CnyNwgAC8", 
    "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 
    "metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s", 
    "vau1zxA2LbssAUEF7Gpw91zMM1LvXrvpzJtmZ58rPsn",  # ←↑-- spl

    "Ed25519SigVerify111111111111111111111111111", 
    "KeccakSecp256k11111111111111111111111111111",   # ←↑-- native precompiles

    "StakeConfig11111111111111111111111111111111",   # ←↓-- some others, I cant find them all.
    "ComputeBudget111111111111111111111111111111",
]