# Validate a block by checking its transactions and hashes
def checkBlockValidity(block, parent, state):
    parentNumber = parent['contents']['blockNumber']
    parentHash = parent['hash']
    blockNumber = block['contents']['blockNumber']
    # Check validity of each transaction in the block
    for txn in block['contents']['txns']:
        if isValidTxn(txn, state):
            state = updateState(txn, state)
        else:
            raise Exception('Invalid transaction in block %s:%s'%(blockNumber, txn))
        # Check hash correctness
        checkBlockHash(block)
        if blockNumber != (parentNumber + 1):
            raise Exception('Hash does not maatch contents of block %s'%blockNumber)
        if block['contents']['parentHash'] != parentHash:
            raise Exception('Parent hash not accurate at block %s'%blockNumber)
        return state