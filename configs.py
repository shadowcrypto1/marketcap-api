chain_configs = {
    'fantom': {
        'main_contract': '0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44',
        'non_circulating_contracts': {
            "veDeus": "0x8B42c6Cb07c8dD5fE5dB3aC03693867AFd11353d",
            "DEUS mSig": "0xEf6b0872CfDF881Cf9Fe0918D3FA979c616AF983",
            "MasterChefV2": "0x120FF9821817eA2bbB700e1131e5c856ccC20d1b",
            "Minter Pool": "0x6E0098A8c651F7A6A9510B270CD02c858C344D94",
            "DUES BAG": "0xC59A3F19bf33D318F4e3eef248ACFE9B37bfc947",
            "AnyswapV6ERC20": "0xf7b38053A4885c99279c4955CB843797e04455f8",
            "gnosis ?": "0x467694A3c9afFfDEB66e2E31F141148287D3Ad1E",
            "TimeBasedMasterChefRewarder": "0x90177BF4f4a5aaF5812508dbC1EBA8752C5cd605",
            "ComplexRewarder": "0xDdB816c59200aF55b1Ca20735Ef086626a2C6a8D",
            "StrategyRewarder": "0x90De614815C1e550213974C2f004C5e56C4a4be0",
            "MasterChefV2 ?": "0x67932809213AFd6bac5ECD2e4e214Fe18209c419",
            "MultiRewarderAccess": "0x9909E6046A9Ca950Cd2a28071338BdcB7d33f9Cb",
            "TimeBasedMasterChefRewarder ?": "0xA81E2bA1035f973c734f1eD23a0c0D6d197dd229",
            "TimeBasedMasterChefRewarder ??": "0x58b86B32F560d025594ADFF02073Ae18976C4700",
            "Admin Wallet": "0xE5227F141575DcE74721f4A9bE2D7D636F923044",
        },
        'http_rpc': 'https://rpcapi.fantom.network'
    },
    'polygon': {
        'main_contract': '0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44',
        'non_circulating_contracts': {
            "bridgePool": "0x1e323B29DeBdd06e5Fa498D380952ae41F46E6E8",
            "Migrator": "0xD6739b3012Dd4179C0Cb45C57e6eADD063983143",
        },
        'http_rpc': 'https://polygon-mainnet-public.unifra.io'
    },
    'arbitrum': {
        'main_contract': '0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44',
        'non_circulating_contracts': {
        },
        'http_rpc': 'https://1rpc.io/arb'
    },
    'bsc': {
        'main_contract': '0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44',
        'non_circulating_contracts': {
        },
        'http_rpc': 'https://bsc-dataseed3.ninicoin.io'
    },
    'eth': {
        'main_contract': '0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44',
        'non_circulating_contracts': {
        },
        'http_rpc': 'https://uk.rpc.blxrbdn.com'
    },
    'metis': {
        'main_contract': '0xDE5ed76E7c05eC5e4572CfC88d1ACEA165109E44',
        'non_circulating_contracts': {
        },
        'http_rpc': 'https://andromeda.metis.io/?owner=1088'
    }
}

update_timeout = 4
redis_prefix = "MARKET_CAP"
