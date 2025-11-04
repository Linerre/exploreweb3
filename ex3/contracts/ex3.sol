// SPDX-License-Identifier: MIT
pragma solidity >=0.8.20;

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract ETHAndTokenTracker {
    address public owner;

    event ETHReceived(address indexed sender, uint256 amount);
    event ETHWithdrawn(address indexed recipient, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    receive() external payable {
        emit ETHReceived(msg.sender, msg.value);
    }

    function depositETH() external payable {
        require(msg.value > 0, "Must send at least some non-zero ETH");
        emit ETHReceived(msg.sender, msg.value);
    }

    function getETHBalance() external view returns (uint256) {
        return address(this).balance;
    }

    function getTokenBalance(address tokenAddress) external view returns (uint256) {
        require(tokenAddress != address(0), "Invalid token address");
        return IERC20(tokenAddress).balanceOf(address(this));
    }

    function withdrawETH() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available in this address");

        uint256 withdrawAmount;

        if (msg.sender == owner) {
            // Owner withdraws all
            withdrawAmount = balance;
        } else {
            // Non-owner withdraws 10%
            withdrawAmount = (balance * 10) / 100;
            require(withdrawAmount > 0, "Withdrawal amount too small");
        }

        // Transfer ETH to the caller
        (bool success, ) = msg.sender.call{value: withdrawAmount}("");
        require(success, "Failed to transfer ETH");

        emit ETHWithdrawn(msg.sender, withdrawAmount);
    }

    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        bool success = IERC20(tokenAddress).transfer(owner, amount);
        require(success, "Token transfer failed");
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
