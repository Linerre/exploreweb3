## What
This is the smart contract in Solidity for Exercise 3 of the take-home assignment required by a job interview.

## How
To build/compile this smart contract, you will need to set up the Ethereum docker container first (in this case, I'm using podman):

``` console
$ podman pull docker.io/ethereum/solc:0.8.30-alpine
```

Then run the below command if you have [GNU Make](https://www.gnu.org/software/make/) installed

``` console
make build
```

Or run the below command

``` console
podman run \
    -v ./contracts/:/sources --name ex3 \
    ethereum/solc:0.8.30-alpine \
    /sources/ex3.sol
    --abi --bin --output-dir /sources/output
```

TODO:
- [ ] Deploy the contract with Truffle or Hardhat
- [ ] Verify the contract and fix any bugs found
