# Check the integrity of the chain and create the current state from a text representation
chainAsText = json.dumps(chain, sort_keys = True)
checkChain(chainAsText)