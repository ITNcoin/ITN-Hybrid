# ITN-Hybrid

This repository has the Solidity code of the Proof of Stake and Proof of Work contract as well as the mining software.

## Staking
The reward structure is as following: after each month, you get 1% staking reward. You can always claim your coins when you decide to do so, the reward will be calculated based on the amount of time you've been staking. The calculation is linear. So that means if you stake for 1/4 month, you get 1/4 %, if you stake 1/2 month, you get 1/2 %, etc. etc.

How to start staking?
- First, go to the token contract here: https://etherscan.io/token/0xf13bb88738dbf1c205c6837614c5551567422e15#writeContract
- Login to MetaMask and click "Connect with Metamask"
- Then, approve the staking contract to take your coins so you can stake them:
-- Look for the box which says: "approve"
-- Once you're there, for the address fill in the POS-contract address: 0x296215d1ee44a7a89ee059d5a9c217dc3298565a
-- For the amount, fill in the desired amount and ADD 18 ZEROS TO IT. So if you want to stake 1 ITN, you will fill in: "1000000000000000000". To make it yourself easy, you can simply copy the zeros: 000000000000000000
- Now, you've approved the staking contract to take your coins and stake them safely where nobody can steal them.
- Go to the staking contract: https://etherscan.io/address/0x296215d1ee44a7a89ee059d5a9c217dc3298565a
- Finally, go to the box which says "mint" and for the "amount" fill in THE SAME amount you approved the contract with (or less, but that'd be a waste!). So in the case described above it will be "1000000000000000000"

And that's it!

If you decide to claim your staking reward, go to the staking contract: https://etherscan.io/address/0x296215d1ee44a7a89ee059d5a9c217dc3298565a#writeContract and click "stopMint". Voilà! You now have more coins!

## Mining

- Download the "ITNMiner.py" file

- If you don't have Python already: download & install Python: https://www.python.org/downloads/

- Download "Build Tools for Visual Studio 2017" from: https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2017

- Select Workloads --> Visual C++ build tools

- Install options: select only the "Windows 10 SDK" (assuming your PC is on Windows 10)

- Run the miner! The miner will guide you through the rest off the process.
