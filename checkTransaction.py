# Number of transactions per block
blockSizeLimit = 5
while len(txnBuffer) > 0:
    bufferStartSize = len(txnBuffer)
    # Get valid transactions
    txnList = []
    while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
        newTxn = txnBuffer.pop()
        validTxn = isValidTxn(newTxn, state)
        if validTxn:
            txnList.append(newTxn)
            state = updateState(newTxn, state)
        else:
            print("ignored transaction")
            sys.stdout.flush()
            # Invalid transaction, move on
            continue
        # Create block
        myBlock = makeBlock(txnList, chain)
        chain.append(myBlock)
