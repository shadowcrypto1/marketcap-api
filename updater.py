import time

from config import update_timeout, REDIS_PREFIX, PRICE_REDIS_TAG
from constants import non_circulating_contracts
from redis_client import redis_client

from utils import RPCManager, deus_spooky


def run_updator():
    managers = {}
    for chain, _ in non_circulating_contracts.items():
        managers[chain] = RPCManager(chain)

    while True:
        for chain, contracts in non_circulating_contracts.items():
            deus_contract = managers[chain].deus_contract
            mc = managers[chain].mc
            print('Checking ' + chain)
            try:
                total_supply = deus_contract.functions.totalSupply().call()
                if contracts:
                    nc_supply = sum(balance[0] for balance in mc.balanceOf(contracts.values()))
                    total_supply -= nc_supply
                print(total_supply)
                redis_client.set(REDIS_PREFIX + chain, total_supply)
            except Exception as ex:
                print('Error:', ex)
                managers[chain].update_rpc()

        try:
            redis_client.set(PRICE_REDIS_TAG, str(deus_spooky()))
        except Exception as ex:
            print('Error:', ex)

        time.sleep(update_timeout)


if __name__ == '__main__':
    run_updator()
