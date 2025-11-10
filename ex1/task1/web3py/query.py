import asyncio
from os import environ
from web3 import Web3, AsyncWeb3

ENDPOINT = "https://mainnet.infura.io/v3/d0b4d2a52c834debbe7fb2481e5c1ac7"

TX_HASH = '0x2ad2bb00718ab0ed8310dacff9c029ea5d41e038d96c9f52561a1e7948759e99'

proxy_url = (environ.get('https_proxy') or environ.get('HTTPS_PROXY') or
             environ.get('http_proxy') or environ.get('HTTP_PROXY'))

req_kwargs = {'proxy': proxy_url, 'timeout': 30}


async def query(tx_hash):
    web3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(ENDPOINT, request_kwargs=req_kwargs))
    tx = await web3.eth.get_transaction(tx_hash)
    print("========= Query using Web3.js =========")
    print('To address:', tx["to"])
    print('Input call data (encoded):', web3.to_hex(tx["input"]))
    print('Gas price:', tx["gasPrice"])


if __name__ == "__main__":
    asyncio.run(query(TX_HASH))
