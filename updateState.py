# Updates the state (account balances) based on a transaction
# txn = transfer amount
# state = account balance
def updateState(txn, state):
    state = state.copy()
    # Updates the state with transaction details
    for key in txn:
        if key in state.keys():
            state[key] += txn[key]
        else:
            state[key] = txn[key]
    return state
