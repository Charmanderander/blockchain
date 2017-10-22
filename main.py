from transaction import *
from hasher import *
from validate import *
from update import *
from blockgen import *

# Random txn generator
txnBuffer = [makeTransaction() for i in range(30)]
state = {u'Alice':50, u'Bob':50}  # Define the initial state

# Generates the genesis block
def genesisblockgen():
    genesisBlockTxns = [state]
    genesisBlockContents = {u'blockNumber':0,u'parentHash':None,u'txnCount':1,u'txns':genesisBlockTxns}
    genesisHash = hashMe( genesisBlockContents )
    genesisBlock = {u'hash':genesisHash,u'contents':genesisBlockContents}
    genesisBlockStr = json.dumps(genesisBlock, sort_keys=True)

    chain = [genesisBlock]

    return chain

# Generates random transactions in the block chain
def blockchaininit(chain,state):
    blockSizeLimit = 5  # Arbitrary number of transactions per block- 
               #  this is chosen by the block miner, and can vary between blocks!

    while len(txnBuffer) > 0:
        bufferStartSize = len(txnBuffer)
    
        ## Gather a set of valid transactions for inclusion
        txnList = []
        while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
            newTxn = txnBuffer.pop()
            validTxn = isValidTxn(newTxn,state) # This will return False if txn is invalid
        
            if validTxn:           # If we got a valid state, not 'False'
                txnList.append(newTxn)
                state = updateState(newTxn,state)
            else:
                print("ignored transaction")
                sys.stdout.flush()
                continue  # This was an invalid transaction; ignore it and move on
        
        ## Make a block
        myBlock = makeBlock(txnList,chain)
        chain.append(myBlock)

    return state

chain = genesisblockgen()
state = blockchaininit(chain,state)

print state
print chain
