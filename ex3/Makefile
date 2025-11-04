VOLUME := ./contracts/
SRC := /sources
DST := /sources/output
CONTRACT := ex3.sol
ETHEREUM := ethereum/solc:0.8.30-alpine

build: $(VOLUME)/$(CONTRACT)
	echo "Compiling the contract"
	podman run -v $(VOLUME):$(SRC) --name ex3 $(ETHEREUM) \
	$(SRC)/$(CONTRACT) --abi --bin --output-dir $(DST)
