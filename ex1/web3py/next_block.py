from web3 import Web3

endpoint = "https://mainnet.infura.io/v3/d0b4d2a52c834debbe7fb2481e5c1ac7"
web3 = Web3(Web3.HTTPProvider(endpoint))

miner = "0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8"
ref = 13507871

def find_next_block():
    curr = ref + 1
    found = False
    max_try = 1000000

    while not found:
        block = web3.eth.get_block(curr)
        if block['miner'].lower() == miner.lower():
            found = True
            print(f"Next block height by {miner} is: {curr}")
            break

        curr += 1

        if curr > ref + max_try:
            print("Block by the same miner not found after 1000000 attempts")
            break

def main():
    find_next_block()


if __name__ == "__main__":
    main()
