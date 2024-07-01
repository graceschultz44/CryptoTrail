# Validate the entire chain
def checkChain(chain):
    # Check that transactions are valid, do not cause an overdraft, that the blocks are 
    # linked by hashes, and returns false if an error was found
    # Data input processing
    if type(chain) == str:
        try:
            chain = json.loads(chain)
            assert(type(chain) == list)
        except:
            return False
    elif type(chain) != list:
        return False
    # Check to see if they are valid updates and that the block hash is valid for 
    # the block contents
    state = {}
    for txn in chain[0]['contents']['txns']:
        state = updateState(txn, state)
    checkBlockHash(chain[0])
    parent = chain[0]
    # Check subsequent blocks, evaluate the reference to the parent block's hash and 
    # the vlaidity of the block number
    for block in chain[1:]:
        state = checkBlockValidity(block, parent, state)
        parent = block
    return state
    