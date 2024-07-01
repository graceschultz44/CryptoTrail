import random
random.seed(0)

# Creates transactions within the stated range
def makeTransaction(maxValue = 3):
    # Randomly chooses -1 or 1 to determine the transaction direction
    sign = int(random.getrandbits(1)) * 2 - 1
    # Randomly choose a transaction amount
    amount = random.randit(1, maxValue)
    person1Pays = sign * amount
    person2Pays = -1 * person1Pays
    return {u'Person1':person1Pays, u'Person2':person2Pays}