# To test the validity of the transactions
state = {u'Person1':5, u'Person2':5}
# Works!
print(isValidTxn({u'Person1':-3, u'Person2':3}, state))
# Creates/destroys tokens
print(isValidTxn({u'Person1':-4, u'Person2':3}, state))
# Causes an overdraft
print(isValidTxn({u'Person1':-6, u'Person2':6}, state))
# Creates a new user
print(isValidTxn({u'Person1':-4, u'Person2':2,'Person3':2}, state))