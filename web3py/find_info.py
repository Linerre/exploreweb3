from collections import Counter
from web3 import Web3

endpoint = "https://mainnet.infura.io/v3/d0b4d2a52c834debbe7fb2481e5c1ac7"
web3 = Web3(Web3.HTTPProvider(endpoint))
height = 13507875

def find_info():
    sender_counter = Counter()
    recv_counter = Counter()
    max_gax_price = 0
    max_gax_tx = None

    block = web3.eth.get_block(height, full_transactions=True)

    for tx in block['transactions']:
        sender = tx['from']
        sender_counter[sender] += 1

        receiver = tx['to']
        if receiver:
            recv_counter[receiver] += 1

        gas = tx['gasPrice']
        if gas > max_gax_price:
            max_gas_price = gas
            max_gas_tx = tx


    most_tx_sender, _ = sender_counter.most_common(1)[0]
    most_tx_recv, _ = recv_counter.most_common(1)[0]
    return most_tx_sender, most_tx_recv, tx

def main():
    sender, recv, tx = find_info()
    print(f"Sender that sent most tx: {sender}")
    print(f"Receiver that received most tx: {recv}")
    print(f"Transaction with highest gas price: {tx}")


if __name__ == "__main__":
    main()
