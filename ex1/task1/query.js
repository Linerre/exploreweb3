import { Web3 } from 'web3';

const ENDPOINT = 'https://mainnet.infura.io/v3/d0b4d2a52c834debbe7fb2481e5c1ac7';
const TX_HASH = '0x2ad2bb00718ab0ed8310dacff9c029ea5d41e038d96c9f52561a1e7948759e99';

async function getTxInfo(txHash) {
    const web3 = new Web3(ENDPOINT);

    try {
        const txInfo = await web3.eth.getTransaction(txHash);
        if (!txInfo) {
            console.error('Faled to get tx info');
            return null;
        }

        const {to, input, gasPrice} = txInfo;
        console.log('========= Query using Web3.js =========')
        console.log('To address:', to);
        console.log('Input call data (raw):', input);
        console.log('Gas Price:', gasPrice);
    } catch (e) {
        console.error('Error getting tx info:', e.message);
        return null;
    }
}

await getTxInfo(TX_HASH);
