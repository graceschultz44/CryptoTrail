# Initializes the genesis block (first block)
# Gives each person 50 coins to start
state = {u'Person1':50, u'Person2':50}
genesisBlockTxns = [state]
genesisBlockContents = {u'blockNumber':0, u'parentHash':None, u'txnCount':1, u'txns':genesisBlockTxns}
genesisHash = hashMe(genesisBlockContents)
genesisBlock = {u'hash':genesisHash, u'contents':genesisBlockContents}
genesisBlockStr = json.dumps(genesisBlock, sort_keys = True)