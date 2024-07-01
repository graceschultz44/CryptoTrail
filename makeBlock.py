# Collect the transactions, create a header, hash it, and add to the chin
def makeBlock(txns, chain):
    parentBlock = chain[-1]
    parentHash = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    txnCount = len(txns)
    blockContents = {u'blockNumber':blockNumber, u'parentHash':parentHash, u'txnCount':len(txns), 'txns':txns}
    blockHash = hashMe(blockContents)
    block = {u'hash':blockHash, u'contents':blockContents}
    return block