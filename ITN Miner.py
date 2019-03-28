# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:08:56 2019

@author: Hilobrain
@title: Python ITN Miner
"""

from web3 import Web3
from web3 import Account
from web3 import eth
from threading import Thread
from time import sleep
from time import clock
from json import load

class term:
    SUCCESS = 5 * "» " + "SUCCESS: "
    WARNING = 5 * "! " + "WARNING: "
    SENSITIVE = 5 * "¡ " + "SENSITIVE: "
    MINING = 5 * "# " + "SUCCESS, MINING: "

class miner:
    def __init__(self, account, contract, contractAddress, challenge, target, gasMode, sleepTime):
        self.ACC = account
        self.contract = contract
        self.contractADDR = contractAddress
        self.challenge = challenge
        self.target = target
        self.gasMode = gasMode
        self.sleepTime = sleepTime
        
    def mine(self):
        while True:
            HASH, HASHINT, nonce = self.mineBlock()
            print(HASH, nonce)
            self.makeTX(HASH, nonce)

    def mineBlock(self):
        solved = False
        nonce = 0
        self.update()
        
        print(term.MINING + "Mining block... ")
        
        start = clock()
        
        while not solved:
            HASH = Web3.soliditySha3(["bytes32", "bytes32", "uint256"], [self.challenge, self.ACC.address, nonce])
            HASHINT = Web3.toInt(HASH)

            if (HASHINT < self.target): 
                solved = True
            else: 
                nonce += 1                
        
        end = clock()
        
        print(nonce / (end - start), " H/S")
        
        return HASH, HASHINT, nonce
    
    def listenForPOW(self):
        while True:
            print("Checking for new POW... ")
            self.update()
            sleep(self.sleepTime)
    
    def update(self):
        self.challenge = self.contract.call().getChallenge()
        self.target = self.contract.call().getMiningTarget()
            
    def buildTX(self, challengeDigest, nonce):   
        TX = contract.functions.mine(nonce, challengeDigest).buildTransaction({
         'from' : self.ACC.address,       
         'chainId': 1,
         'gas': 200000,
         'gasPrice': Web3.toWei(str(self.gasMode), 'gwei'),
         'nonce': web3.eth.getTransactionCount(self.ACC.address)
        })
    
        signed_TX = eth.Account.signTransaction(TX, private_key = self.ACC.privateKey)       
        print(signed_TX)
        
        return TX, signed_TX
    
    def makeTX(self, HASH, nonce):
        TX, signed_TX = self.buildTX(HASH, nonce)
        TX_HASH = web3.eth.sendRawTransaction(signed_TX.rawTransaction) 
        sleep(5)            #don't spam WEB3 provider with waitForTXReceipt...
        try:
            web3.eth.waitForTransactionReceipt(TX_HASH, timeout = 300)
        except:
            print(term.WARNING + "The transactions require a bit more gas! Adding 0.5")
            self.gasMode += 0.5
            self.makeTX(HASH, nonce)
            
        print(term.SUCCESS + "Succesfully mined block... ", end = 2*"\n")
        
        return True
              
def initContract(contractAddress):
    web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/" + projectID))

    with open('ABI.json', 'r') as abi_definition:
        abi = load(abi_definition)
    
    contract = web3.eth.contract(contractAddress, abi=abi)  
    
    return web3, contract

def createAccount():
    ACC = Account.create("RANDOMSTRINGTOINCREASETHEENTROPYOFTHEHASH!")
    print(term.SUCCESS + "Account public key: " + ACC.address)
    print(term.SENSITIVE + "Account PRIVATE KEY: " + ACC.privateKey.hex(), end = 2*"\n")    
   
    return ACC

def getChallenge():
    newChallenge = contract.call().getChallenge()  
     
    return Web3.toHex(newChallenge)

def getTarget():
    newTarget = contract.call().getMiningTarget()
    
    return newTarget


print("""$$$$$$\ $$$$$$$$\ $$\   $$\       $$\      $$\ $$\                               
\_$$  _|\__$$  __|$$$\  $$ |      $$$\    $$$ |\__|                              
  $$ |     $$ |   $$$$\ $$ |      $$$$\  $$$$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  
  $$ |     $$ |   $$ $$\$$ |      $$\$$\$$ $$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ 
  $$ |     $$ |   $$ \$$$$ |      $$ \$$$  $$ |$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
  $$ |     $$ |   $$ |\$$$ |      $$ |\$  /$$ |$$ |$$ |  $$ |$$   ____|$$ |      
$$$$$$\    $$ |   $$ | \$$ |      $$ | \_/ $$ |$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\______|   \__|   \__|  \__|      \__|     \__|\__|\__|  \__| \_______|\__|      
                                                                                                                       """)

answer = input("It is recommended to generate a new private-key to mine to. Do you want to create one? [Y/N] ")        

if (answer.upper() == "Y"):
    print(term.WARNING + "WARNING, KEEP THESE KEYS SAFE. LOSE OF KEYS MEANS LOSE OF FUNDS.", end = 2*"\n")
    print(createAccount(), end = 2*"\n") 
    print(term.SUCCESS + "Succesfully created keys. Make sure to write these down somwhere.", end = 2*"\n")

elif (answer.upper() == "N"):
    print(term.WARNING + "It is recommended to create a NEW address for this miner!", end = 2*"\n")

while True:
    try:   
        privKey = input("Private-key to mine to (it's recommended to create a NEW address for this!): ")      
        account = eth.Account.privateKeyToAccount(privKey)
        break
    except:
        print("This is not a valid private key, try again please.", end = 2*"\n")
        continue
while True:
    try:
        advanced = input("Enter advanced options? [Y/N] ")
        if (advanced.upper() == "Y"):            
            while True:
                try:
                    gasMode = 2 * int(input("Do you want slow (cheap), normal or fast (expsensive) transactions? [1,2,3] For more information, see the documentation. "))
                    if not gasMode in [2,4,6]:
                        raise
                    break
                except:
                    print("Please enter a valid option.", end = 2*"\n")
                    
            while True:
                try:
                    sleepTime = int(input("Sleeping time between contract-update checks in seconds, recommended is 5 seconds: "))
                    if (sleepTime < 1):
                        raise
                    break
                except:
                    print("Please enter a valid value. ", end = 2*"\n")
            break
        elif (advanced.upper() == "N"):
            gasMode, sleepTime = 4, 5
            break
        else:
            raise
    except:
        print("Please chose a valid option. ")
        
contractAddress = "0x29B7b3Cc8D6a8ef9153e67CAB128C3A603DCb674"
projectID = "815ca6b994884e5184182d8dfd9cf96a"
web3, contract = initContract(contractAddress)

miner1 = miner(account, contract, contractAddress, getChallenge(), getTarget(), gasMode, sleepTime)

miningThread = Thread(target = miner1.mine, args = [])
listenForPOWThread = Thread(target = miner1.listenForPOW, args = [])

miningThread.start()
listenForPOWThread.start()
miningThread.join()
listenForPOWThread.join()
