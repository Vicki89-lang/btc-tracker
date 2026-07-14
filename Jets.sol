// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Jets is ERC20 {
    address public impactWallet;
    uint256 public impactFeeBps = 100;

    constructor(address _impactWallet) ERC20("Jets", "JETS") {
        impactWallet = _impactWallet;
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function _transfer(address from, address to, uint256 amount) internal override {
        uint256 fee = (amount * impactFeeBps) / 10000;
        uint256 sendAmount = amount - fee;
        
        super._transfer(from, impactWallet, fee);
        super._transfer(from, to, sendAmount);
    }