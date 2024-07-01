# Check if the block hash matches the expected hash
def checkBlockHash(block):
    expectedHash = hashMe(block['content'])
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block %s'% block['contents']['blockNumber'])
    return