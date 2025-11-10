import { Web3 } from 'web3';
import { HttpsProxyAgent } from 'https-proxy-agent';

const ENDPOINT = 'https://mainnet.infura.io/v3/d0b4d2a52c834debbe7fb2481e5c1ac7';
const TX_HASH = '0x2ad2bb00718ab0ed8310dacff9c029ea5d41e038d96c9f52561a1e7948759e99';

async function getTxInfo(txHash) {
    // I'm living behind GFW so I need the proxy. You probably don't.
    const proxyUrl = process.env.https_proxy || process.env.HTTPS_PROXY;
    const proxyAgent = new HttpsProxyAgent(proxyUrl);

    const web3 = new Web3(new Web3.providers.HttpProvider(
        ENDPOINT,
        {
            providerOptions: { agent: proxyAgent }
        }
    ));

    try {
        const txInfo = await web3.eth.getTransaction(txHash);
        if (!txInfo) {
            console.error('Faled to get tx info');
            return null;
        }

        const {to, input, gasPrice} = txInfo;
        console.log('========= Query using Web3.js =========')
        console.log('To address:', to);
        console.log('Input call data (encoded):', input);
        console.log('Gas Price:', gasPrice);
    } catch (e) {
        console.error('Error getting tx info:', e.message);
        return null;
    }
}

await getTxInfo(TX_HASH);
