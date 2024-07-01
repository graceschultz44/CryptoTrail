# Check the new block and update the state of it if it is deemed a valid block
print("Blockchain on Node A is currently %s blocks long"%len(chain))
try:
    print("New Block Received; checking validity...")
    state = checkBlockValidity(newBlock, chain[-1], state)
    chain.append(newBlock)
except:
    print("Invalid block; ignoring and waiting for the next block")
print("Blockchain on Node A is now %s blocks long"%len(chain))
