# ITN-Hybrid

This repository has the Solidity code of the Proof of Stake and Proof of Work contract as well as the mining software.

## Staking
The reward structure is as following: after each month, you get 1% staking reward. You can always claim your coins when you decide to do so, the reward will be calculated based on the amount of time you've been staking. The calculation is linear. So that means if you stake for 1/4 month, you get 1/4 %, if you stake 1/2 month, you get 1/2 %, etc. etc.

How to start staking?
- First, go to the token contract here: https://etherscan.io/token/0xf13bb88738dbf1c205c6837614c5551567422e15#writeContract
- Login to MetaMask and click "Connect with Metamask"
- Then, approve the staking contract to take your coins so you can stake them:
-- Look for the box which says: "approve"
-- Once you're there, for the address fill in the POS-contract address: [ADDRESS]
-- For the amount, fill in the desired amount and ADD 18 ZEROS TO IT. So if you want to stake 1 ITN, you will fill in: "1000000000000000000". To make it yourself easy, you can simply copy the zeros: 000000000000000000
- Now, you've approved the staking contract to take your coins and stake them safely where nobody can steal them.
- Go to the staking contract: [LINK OF STAKING ADDRESS]
- Click "mint" and fill in THE SAME amount you approved the contract with. So in the case described above it will be "1000000000000000000"

And that's it!

If you decide to claim your staking reward, go to the staking contract: [] and click "stopMint". Voilà! You now have more coins!
