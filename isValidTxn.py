# Checks if a transaction is valid
def isValidTxn(txn, state):
    # Make sure that the sum of withdrawals and deposits is not 0
    if sum(txn.values()) is not 0:
        return False
    # Verify that the current transaction will not cause an overdraft
    for key in txn.keys():
        if key in state.keys():
            acctBalance = state[key]
        else:
            acctBalance = 0
        if (acctBalance + txn[key]) < 0:
            return False
    return True